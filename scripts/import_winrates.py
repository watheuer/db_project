import csv
from champion_picker.models import Champion, Role, WinRate
from os import getcwd

csvpath = '/scripts/CSV Files'

with open(getcwd() + csvpath + '/winrate.csv', 'rb') as f:
    skip = 1
    reader = csv.reader(f)
    for row in reader:
        if skip == 1:
            skip = 0
            continue
        champ = row[0]
        opponent = row[1]
        role = row[2]
        winrate = row[3]
        champion1 = Champion.objects.get(name=champ)
        champion2 = Champion.objects.get(name=opponent)
        role1 = Role.objects.get(champion=champion1, name=role)
        role2 = Role.objects.get(champion=champion2, name=role)
        win_rate = WinRate.objects.create(role1=role1, role2=role2, win_rate=winrate)
        win_rate.save()