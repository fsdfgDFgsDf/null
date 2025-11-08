import os

def exec(cmd):
    os.system(cmd)

def setup():
    exec('python src/ex/title.py')
    exec('python src/ex/size.py')

def start():
    exec('python src/main/main.py')

setup()
start()