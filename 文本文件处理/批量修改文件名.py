#encoding=utf8
'''
ָ���ļ��У��޸��ļ�����ָ���ļ����͵��ļ���
'''

import os
def change_suffix(dir_path):
for name in os.listdir(dir_path):
new_name=name.replace('.markdown','.md')
os.rename(name,new_name)
change_suffix(".")