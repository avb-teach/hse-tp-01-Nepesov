#!/usr/bin/env python3

#делаем шебанг для использования python

import sys
import os
import shutil 

input_directory = sys.argv[1]
output_directory = sys.argv[2]
os.makedirs(output_directory,exist_ok = True)

#https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level12.lecture06
#https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/