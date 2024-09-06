import os
from pprint import pprint # библиотека для вывода словаря с табуляцией (красивый вывод)


def categorize_files_by_type(folder_path):
    file_dict = {} # создаю пустой словарь
    files = os.listdir(folder_path) # записываю в files список имеющихся файлов.
    

    for root, dirs, files in os.walk(folder_path): 
        for file in files: #пробегаемся по файлам
            basename, extension = os.path.splitext(file) # разбиваем файл на название и тип расширение.

            if extension == '':
                extension = ''

            if extension not in file_dict:
                file_dict[extension] = []
            file_dict[extension].append(os.path.abspath(file))

    return pprint(file_dict)


# путь к папке
folder_path = r"c:\Users\yguly\Downloads"

# обработчики ошибок
if os.path.exists(folder_path) == False:
    raise FileNotFoundError(f"Указанный путь некорректный")
if os.path.isdir(folder_path) == False: 
    raise NotADirectoryError(f"Указанный файл не является папкой")

categorize_files_by_type(folder_path)


