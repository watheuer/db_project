from __future__ import unicode_literals

from django.db import models

# from champion.gg: /champion/:name/general?api_key=<KEY>
class Champion(models.Model):
    name = models.CharField(max_length=32)
    portrait_image = models.ImageField(upload_to='champ_images', blank=True, null=True)
    q_skill = models.CharField(max_length=32)
    w_skill = models.CharField(max_length=32)
    e_skill = models.CharField(max_length=32)
    r_skill = models.CharField(max_length=32)
    # other shit like the image
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=32)
    lane = models.CharField(max_length=32, default='')
    champion = models.ForeignKey(Champion, null=True, on_delete=models.SET_NULL)
    win_rate = models.DecimalField(max_digits=30, decimal_places=2)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    minions_killed = models.IntegerField()

    def __str__(self):
        return "[%s] %s %s" % (self.name, self.champion, self.lane)

class WinRate(models.Model):
    champ1 = models.ForeignKey(Role, related_name='champ1')
    champ2 = models.ForeignKey(Role, related_name='champ2')
    win_rate = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return "%s %s" % (self.champ1, self.champ2)

class Item(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ItemBuild(models.Model):
    name = models.CharField(max_length=48)
    champion = models.ForeignKey(Champion)
    items = models.ManyToManyField(Item, related_name='items')

    def __str__(self):
        return "[%s] %s" % (self.champion, self.name)
