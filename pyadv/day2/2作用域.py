#coding:gbk
# Time:2020-03-17 21:54
# Author:TSL

"""
�������ǳ�������ʱ�����ɱ����ʵķ�Χ
      �����ں����ڵı����Ǿֲ�����
      ������ģ�������ı�����ȫ�ֱ���
"""


g = 99                 #ȫ�ֱ�����������ģ�鵱�У�ֻ�ڵ�ǰģ����Ч

def foo():
    l = 100            #�ֲ��������������ں��������

    print(g)
    print(l)

    def inner():
        e = 300
        print(e)       #Ƕ��������

foo()
print(g)
# print(l)

print(__name__)        #����������python�ڲ�����
# __main__


# L (Local)      �ֲ�������
# E (Enclosing)  Ƕ��������
# G (Global)     ȫ��������
# B (Built-in)   ����������
















































































































