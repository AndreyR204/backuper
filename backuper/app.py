import configparser
from pathlib import Path
from subprocess import Popen


def config_changer(args):
    config = configparser.ConfigParser()
    config2 = configparser.ConfigParser()
    if not Path('conf.ini').is_file():
        proc = Popen("python backuper/backuper.pyw")
        address1 = input('Enter FTP server address:')
        port1 = input('Enter FTP server port: ')
        login1 = input('Enter login for FTP: ')
        password1 = input('Enter password for FTP: ')
        config['FTP'] = {'login1': str(login1), 'password1': str(password1), 'address1': str(address1),
                         'port1': str(port1)}
        login2 = input('Enter token for Yandex Disk: ')
        config['Yandex Disk'] = {'login2': str(login2)}
        config['Times'] = {'time1': input('Enter time for FTP: ')}
        config['Times']['time2'] = input('Enter time for Yandex Disk: ')
        config['Lists'] = {'list1': input('Enter list for FTP: ')}
        config['Lists']['list2'] = input('Enter list for Yandex Disk: ')
        config['Process'] = {'stop': str(False)}
    else:
        if args.set1:
            address1 = input('Enter FTP server address:')
            port1 = input('Enter FTP server port: ')
            login1 = input('Enter login for FTP: ')
            password1 = input('Enter password for FTP: ')
            config['FTP'] = {'login1': str(login1), 'password1': str(password1), 'address1': str(address1),
                             'port1': str(port1)}
        else:
            config2.read('conf.ini')
            config['FTP'] = config2['FTP']
        if args.set2:
            login2 = input('Enter token for Yandex Disk: ')
            config['Yandex Disk'] = {'login2': str(login2)}
        else:
            config2.read('conf.ini')
            config['Yandex Disk'] = config2['Yandex Disk']
        if args.time1 != 0:
            config['Times'] = {'time1': str(args.time1)}
        else:
            config2.read('conf.ini')
            config['Times'] = {'time1': config2['Times']['time1']}
        if args.time2 != 0:
            config['Times'] = {'time2': str(args.time2)}
        else:
            config2.read('conf.ini')
            config['Times'] = {'time2': config2['Times']['time2']}
        config['Process'] = {'stop': str(args.stop)}
        if args.list1 is not None:
            config['Lists'] = {'list1': str(args.list1)}
        else:
            config2.read('conf.ini')
            config['Lists'] = {'list1': config2['Lists']['list1']}
        if args.list2 is not None:
            config['Lists'] = {'list2': str(args.list2)}
        else:
            config2.read('conf.ini')
            config['Lists'] = {'list2': config2['Lists']['list2']}
    with open('conf.ini', 'w') as configfile:
        config.write(configfile)
    config.read('conf.ini')
    if config['Process']['stop'] == 'True':
        proc = Popen("python backuper/backuper.pyw")
