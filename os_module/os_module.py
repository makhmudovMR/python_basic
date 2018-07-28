import os

'''
Модуль os предоставляет множество функций для работы с операционной системой, 
причём их поведение, как правило, не зависит от ОС, 
поэтому программы остаются переносимыми.

Здесь будут приведены наиболее часто используемые из них.
'''

currDir = os.getcwd()
print('current dir', currDir)
listdir = os.listdir()
print(listdir)
if 'hello_world' not in listdir:
    print('make dir hello world......')
    os.mkdir('hello_world')

import time

time.sleep(6)

os.rename('hello_world', 'new_dir')

time.sleep(6)

os.rmdir('new_dir')
