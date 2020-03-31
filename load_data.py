# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    files = [f for f in listdir('./fixtures') if isfile(join('./fixtures', f)) and f.endswith('.json')]
    for f in files:
        os.system('python manage.py loaddata fixtures/%s' % f)
