def file_reading ():
    import glob
    import pathlib
    import os
    from pathlib import Path
    path = Path(pathlib.Path.cwd(),'task3') #Задаем относительный путь к папке
    files_dict = {}
    for files in glob.glob(os.path.join(path, '*.txt')): #Фильтруем файлы по формату
        with open (files, "r", encoding="utf-8" ) as file:
            #Созжаем словарь ключом которого будет кол-во строк, значением имя файла
            files_dict[sum(1 for line in file)] = os.path.basename(files)
    #Создаем относительный путь для создания файла
    new_file_name="file_to_write"
    new_file_path=os.path.join(path, new_file_name + ".txt")
    with open (new_file_path,'w', encoding='utf-8') as file_to_write:
        for keys in sorted(files_dict):  # Ключи в словаре отсортированы от меньшего к большему
            with open (os.path.join(path,files_dict[keys]),'r', encoding='utf-8') as file_to_read:
                # Записываем название файла
                file_to_write.write(str(files_dict[keys]) + "\n")
                # Записываем количество строк
                file_to_write.write(str(keys) + '\n')
                # Записываем содержимое исходного файла
                file_to_write.write(file_to_read.read() + '\n')
file_reading()