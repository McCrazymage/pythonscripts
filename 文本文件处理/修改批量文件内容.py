#encoding:utf8
'''
ָ���ļ��У�ָ���ļ����ͣ��滻���ļ�����ȫ���ļ������ݡ�
ע����window�µĶ�д������Ҫָ�����룬����Ҫ���ļ�ͷָ��#coding:utf-8 ���룬
������ֱ������⡣
'''


import os
import os.path

path='.'
oldStr='.php'
newStr='.html'

for (dirpath, dirnames, filenames) in os.walk(path):
    for file in filenames:
        if os.path.splitext(file)[1]=='.html':
            print(file)
            filepath=os.path.join(dirpath,file)
            try:
                text_file = open(filepath, "r")
                lines = text_file.readlines()
                text_file.close()
                output  = open(filepath,'w')
                for line in lines:
                    #print(line)
                    if not line:
                        break
                    if(oldStr in line):
                        tmp = line.split(oldStr)
                        temp = tmp[0] + newStr + tmp[1]
                        output.write(temp)
                    else:
                        output.write(line)
                output.close()
            except Exception:
                print(Exception)
                break