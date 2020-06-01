import schedule
from subprocess import Popen
import configparser


def process_executter(stop):
    proc = Popen("python backuper/backuper.pyw")
    if stop:
        proc.terminate()
        proc.wait()
    else:
        proc.call()

