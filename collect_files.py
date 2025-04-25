#!/usr/bin/env python3

#делаем шебанг для использования python

import sys
import os
import shutil 

input_directory = None
output_directory = None
max_depth = None 

args = sys.argv[1:]
i = 0 

while i < len(args):
    if args[i] == "--max_depth":
        try:
            if i+1 >= len(agrs):
                raise IndexError
            max_depth = int(args[i+1])
            if max_depth < 0:
                raise ValueError
        except: 
            sys.exit(1)
        i +=2
    else:
        if not input_directory:
            input_directory = args[i]
        else:
            output_directory = args[i]
        i +=1
    

os.makedirs(output_directory,exist_ok = True)

accounting = {}

for current_dir, other_directories, files in os.walk(input_directory):
    for name in files:
        files_src = os.path.join(current_dir,name)
        file_name , extension = os.path.splitext(name)

        if name not in accounting:
            accounting[name] = 0
         
        count = accounting[name]

        if count == 0:
            cur_name = name
        else:
            cur_name = f"{file_name}_{count}{extension}" if extension else f"{name}_{count}"
        
        

        copied_file_path = os.path.join(output_directory, cur_name)
        shutil.copy(files_src , copied_file_path)

        accounting[name] +=1



    rel_path = os.path.relpath(current_dir,input_directory)
    depth = 0 if rel_path == "." else rel_path.count(os.sep) + 1

    if max_depth != None and depth >= max_depth:
        del other_directories[:]
     

#https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level12.lecture06
#https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/
#https://pythoner.name/walk
#https://www.tutorialspoint.com/python/os_path_relpath.htm
#https://ru.stackoverflow.com/questions/1345669/%D0%9A%D0%B0%D0%BA%D0%BE%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BC%D0%B5%D0%B5%D1%82-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-os-sep
#https://dzen.ru/a/Xl01D6yaI23T2TBQ