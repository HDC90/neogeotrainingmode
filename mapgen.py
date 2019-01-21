try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp


# Classe ConfigParser
config = cp.ConfigParser()


# mapping des controles du p1
print('mapping des controles du p1')
config.add_section('p1 controls')
config.set('p1 controls', 'P1-up', input('P1-up input '))
config.set('p1 controls', 'P1-left', input('P1-left input '))
config.set('p1 controls', 'P1-down', input('P1-down input '))
config.set('p1 controls', 'P1-right', input('P1-right input '))
config.set('p1 controls', 'P1-A', input('P1-A input '))
config.set('p1 controls', 'P1-B', input('P1-B input '))
config.set('p1 controls', 'P1-C', input('P1-C input '))
config.set('p1 controls', 'P1-D', input('P1-D input '))
print('mapping p1 terminé')


# mapping des controles du dummy
print('mapping des controles du p2')
config.add_section('p2 controls')
config.set('p2 controls', 'P2-up', input('P2-up input '))
config.set('p2 controls', 'P2-left', input('P2-left input '))
config.set('p2 controls', 'P2-down', input('P2-down input '))
config.set('p2 controls', 'P2-right', input('P2-right input '))
config.set('p2 controls', 'P2-A', input('P2-A input '))
config.set('p2 controls', 'P2-B', input('P2-B input '))
config.set('p2 controls', 'P2-C', input('P2-C input '))
config.set('p2 controls', 'P2-D', input('P2-D input '))
print('mapping p2 terminé')


# mapping fonction record
print('mapping fonction record')
config.add_section('record controls')
config.set('record controls', 'record', input('Record input '))
config.set('record controls', 'stop', input('Stop input '))
config.set('record controls', 'play', input('Play input '))
print('mapping record terminé')


# Ecrire le fichier de configuration
with open('neomapconf.ini', 'w') as settings:
    config.write(settings)
