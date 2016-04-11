from __future__ import unicode_literals

from django.db import models

# from champion.gg: /champion/:name/general?api_key=<KEY>
class Champion(models.Model):
    name = models.CharField(max_length=32)
    # other shit like the image

class Role(models.Model):
    name = models.CharField(max_length=32)
    champion = models.ForeignKey(
        'Champion',
        on_delete=models.SET_NULL
    )
    win_rate = models.DecimalField(decimal_places=2)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    minions_killed = models.IntegerField()
    q_skill = models.CharField(max_length=32)
    w_skill = models.CharFIeld(max_length=32)
    e_skill = models.CharFIeld(max_length=32)
    r_skill = models.CharFIeld(max_length=32)

class WinRate(models.Model):
    champ1 = models.ForeignKey('Role')
    champ2 = models.ForeignKey('Role')
    win_rate = models.DecimalField(decimal_places=2)

