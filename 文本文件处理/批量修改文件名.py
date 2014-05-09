#encoding=utf8
'''
指定文件夹，修改文件夹下指定文件类型的文件名
'''

import os
def change_suffix(dir_path):
for name in os.listdir(dir_path):
new_name=name.replace('.markdown','.md')
os.rename(name,new_name)
change_suffix(".")