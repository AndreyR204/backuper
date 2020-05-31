import schedule
import configparser


def job():
    pass


def config_changer(args):
    if args.set1:
        login1 = input('Enter login for FTP: ')
        password1 = input('Enter password for FTP: ')
    if args.set2:
        login2 = input('Enter login for 2: ')
        password2 = input('Enter password for 2: ')
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'login1': login1, 'login2': login2, 'password1': password1,
                         'password2': password2,'time1': args.time1, 'time2': args.time2}
    with open('conf.ini', 'w') as configfile:
        config.write(configfile)
