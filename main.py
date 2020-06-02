#!/usr/bin/env python3
import argparse
from config import config
from backuper import app

parser = argparse.ArgumentParser()
parser.add_argument('--set1', help='authorisation for FTP', action='store_true')
parser.add_argument('--set2', help='authorisation for 2', action='store_true')
parser.add_argument('--list1', '-l1', default=None, help='txt file with listed directories to backup on FTP')
parser.add_argument('--list2', '-l2', default=None, help='txt file with listed directories to backup on 2')
parser.add_argument('--time1', '-t1', default=config.time1, help='period of backuping in minutes')
parser.add_argument('--time2', '-t2', default=config.time2, help='period of backuping in minutes')
parser.add_argument('--stop', help='stop backuping', action='store_true')
parser.add_argument('--status', help='status of process')
args = parser.parse_args()
app.config_changer(args)