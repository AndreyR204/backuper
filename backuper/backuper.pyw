import ftplib
import configparser
import schedule
import os
import yadisk


def ftp_sender():
    try:
        f = open(config['Lists']['list1'])
    except FileNotFoundError:
        return
    try:
        ftp = ftplib.FTP(config['FTP']['address1'], config['FTP']['login1'], config['FTP']['password1'],
                         None, None, (config['FTP']['address1'], config['FTP']['port1']))
        ftp.login()

        for dir in f:
            for file in os.listdir(dir):
                file_to_upload = open(file, 'rb')
                ftp.storbinary('STOR ' + file, file_to_upload)
    except ConnectionError:
        return


def two_sender():
    f = open(config['Lists']['list2'])
    y = yadisk.YaDisk(token=config['Yandex Disk']['login2'])
    for dir in f:
        for file in os.listdir(dir):
            str = "/" + file
            y.upload(file, str)


global config
config = configparser.ConfigParser()
config.read('conf.ini')
global time1, time2
time1 = int(config['Times']['time1'])
time2 = int(config['Times']['time2'])
schedule.every(time1).minutes.do(ftp_sender())
schedule.every(time2).minutes.do(two_sender())

while config['Process']['stop']:
    schedule.run_pending()
    time1 = int(config['Times']['time1'])
    time2 = int(config['Times']['time2'])
