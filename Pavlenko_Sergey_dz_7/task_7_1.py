# Задание 1

import os

struct_prjct = {'my_project': ['setings', 'mainapp', 'adminapp', 'authapp']}

for root, folders in struct_prjct.items():
    if not os.path.exists(root):
        for folder in folders:
            dir = os.path.join(root, folder)
            os.makedirs(dir)

