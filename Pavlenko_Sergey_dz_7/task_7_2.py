# Задание 2

import os
import yaml

with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file) # открыли файл и прочитали из него

def create_struct_prjct(data_struct):
    for folder, datas in data_struct.items(): # проходим по словарю
        if not os.path.exists(folder): # если не существует, создаем корневую папку
            os.mkdir(folder)
            os.chdir(folder) # переходим в созданную корневую папку
            for data in datas:
                if isinstance(data, dict): # если словарь - создаем папку
                    create_struct_prjct(data)
                else:
                    if not os.path.exists(data): # иначе если не существует
                        if '.' in data: # и файл, создаем файл и записываем пустую строку
                            with open(data, 'w') as f:
                                f.write('')
    else:
        os.chdir('../')

if __name__ == '__main__':
    create_struct_prjct(d)
