import configparser
from backuper import launcher


def config_changer(args):
    config = configparser.ConfigParser()
    if args.set1:
        address1 = input('Enter FTP server address:')
        port1 = input('Enter FTP server port: ')
        login1 = input('Enter login for FTP: ')
        password1 = input('Enter password for FTP: ')
        config['FTP'] = {'login1': str(login1), 'password1': str(password1), 'address1': str(address1), 'port1': str(port1),
                         'time1': str(args.time1), 'list1': str(args.list1)}
    if args.set2:
        login2 = input('Enter login for 2: ')
        password2 = input('Enter password for 2: ')
        config['2'] = {'login2': login2, 'password2': password2, 'time2': args.time2, 'list2': args.list2}
    with open('conf.ini', 'w') as configfile:
        config.write(configfile)
    if args.stop:
        launcher.process_executter(True)
    else:
        launcher.process_executter(False)
