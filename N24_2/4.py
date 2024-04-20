f = open('N24_2\\4.txt').read()

print(f.count('BOSS') + f.count('JBOSS') - f.count('JBOSSJ') + f.count('BOSSJ'))