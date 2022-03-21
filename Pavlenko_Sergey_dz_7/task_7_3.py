# Задание 3

import os
import shutil

html_list = []
os.chdir('my_project')

if not os.path.exists('templates'):
    os.mkdir('templates')  # создаем папку templates куда будем копировать шаблоны
direct = '/home/pav/PycharmProjects/pythonProject/my_project/templates'  # сохраним путь к templates в переменную

for r, d, f in os.walk(os.getcwd()):  # os.walk возвращает путь к директории, список поддиректорий и файлов в директории
    for file in f:
        if file.endswith('.html'):  # делаем проверку на нужные нам шаблоны
            html_list.append(os.path.join(r, file))  # собираем список путей к шаблонам

print(html_list)

for html in html_list:
    folder = os.path.join(direct, os.path.basename(os.path.dirname(html)))
    # записываем в переменную путь к будущим поддиректориям в templates, в которых будем хранить копии шаблонов
    # os.path.dirname(html) - возвращает имя шаблона, а os.path.basename(os.path.dirname(html) - имя директории шаблона
    if not os.path.exists(folder):
        os.mkdir(folder) # создаем соответствующие поддиректории в директории templates
    shutil.copy(html, folder) # копируем шаблоны в соответствующие поддиректории
