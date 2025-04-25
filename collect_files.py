#!/usr/bin/env python3

#делаем шебанг для использования python

import sys # импортируем sys для получения аргументов
import os #os для получения путей и проходок по полученным аргументам walk, makedirs and path 
import shutil #shutil нужен для копирования src-ишников 

input_directory = None #оставляем переменные в состоянии None тк нам изначально неизвестна последовательность получения аргументов
output_directory = None
max_depth = None 

# получаем аргументы 
args = sys.argv[1:]
#счетчик аргов
i = 0 

#попытка получения аргумента --max_depth с выводом ошибок, определение входных и выходеных директорий 
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

# создает директории в выходной директории, и если папка сущ -> пропуск из-за второго параметра
os.makedirs(output_directory,exist_ok = True)
#создание учетного словаря для сохранения имен файлов 
accounting = {}

#проход по аргументам подданым изначально current_dir - нынешняя директория, other_directories - другие директории , files -файлы
for current_dir, other_directories, files in os.walk(input_directory):
    for name in files: # проход по файлам, для просмотра имен
        files_src = os.path.join(current_dir,name) # сборка пути к файлу "./../../name.ext"
        file_name , extension = os.path.splitext(name) # разделение на именную часть и расширение файла
# создание счетчика для уникальности имен файлов
        if name not in accounting:
            accounting[name] = 0
        
        count = accounting[name]

        if count == 0:
            cur_name = name
        else:
            cur_name = f"{file_name}_{count}{extension}" if extension else f"{name}_{count}" # создаем полное имя файла для неповторений, 
            #с условием наличия расширения 
        
        

        copied_file_path = os.path.join(output_directory, cur_name) # создает путь для копии файла output_directory- куда копируем , cur_name - сгенерированное имя 
        shutil.copy(files_src , copied_file_path) # копирует файл из files_src в copied_file_path

        accounting[name] +=1 # плюс 1 к счетчику 



    rel_path = os.path.relpath(current_dir,input_directory) # переменная для определения глубины  внутри  input_directory
    depth = 0 if rel_path == "." else rel_path.count(os.sep) + 1 # глубина 0, если текущ папка = входной, иначе количество /(os.sep) будет увеличено 

    if max_depth is not None and depth >= max_depth: #  проверка не превышена ли макс глубина
        del other_directories[:] #если превышена то очистить список этих папок иначе зачем их проверять ? 
     

#https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level12.lecture06
#https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/
#https://pythoner.name/walk
#https://www.tutorialspoint.com/python/os_path_relpath.htm
#https://ru.stackoverflow.com/questions/1345669/%D0%9A%D0%B0%D0%BA%D0%BE%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BC%D0%B5%D0%B5%D1%82-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-os-sep
#https://dzen.ru/a/Xl01D6yaI23T2TBQ