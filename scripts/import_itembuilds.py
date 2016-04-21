import csv
from champion_picker.models import Role, Item, ItemBuild
from os import getcwd

csvpath = '/scripts/CSV Files'

with open(getcwd() + csvpath + '/itembuild.csv', 'rb') as f:
    skip = 1
    reader = csv.reader(f)
    for row in reader:
        if skip == 1:
            skip = 0
            continue
        name = row[0]
        champ = row[1]
        rolename = row[2]
        items = row[3].split(',')
        role = Role.objects.get(champion=champ, name=rolename)
        build = ItemBuild(name=name, role=role)
        build.save()
        for pk in items:
            item = Item.objects.get(pk=pk)
            build.items.add(item)
        build.save()
