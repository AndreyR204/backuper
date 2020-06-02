import schedule
from subprocess import Popen
import configparser


def process_executter(stop):
    global proc
    if stop:
        proc.terminate()
        proc.wait()
    else:
        try:
            proc.terminate()
        except NameError:
            pass
        proc = Popen("python backuper/backuper.pyw")
        pid = proc.pid

