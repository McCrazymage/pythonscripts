#encoding:utf8
'''
指定文件夹，指定文件类型，替换该文件夹下全部文件的内容。
注意在window下的读写内容需要指定编码，还需要在文件头指定#coding:utf-8 编码，
避免出现编码问题。
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