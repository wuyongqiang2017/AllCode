#coding:gbk
print("���к�")

'''
������Python2������Python3���ڴ��е���Զ��Unicode�ֽڣ���������ִ�е�ʱ��Python2�ͼ�����
��Python2��ִ�е�ʱ���������ڿ����ġ����к��������ǿ�����
���ͱ����ĵظ�Ϊ�ֽ���ʽ�������ڴ��У���Ϊ���Ǳ�����GBK����������GBK�ֽڴ������ڴ��еģ�������Ҫִ��������Ҫ�ѡ����к���
תΪ����չ�ָ����ǣ�ֻ���ȱ�ΪUnicode����ܱ�����ģ�������ʱ�����ǵ�����ͷ�������ͨ��ʲô��ʽ��ΪUnicode��
��Ȼ��GBK�ֽڵ�ȻҪ��gbk��������Unicode�Բ��ԣ������������û��decode�������Ļ����������pychm����Ĭ�ϵ�utf-8
ȥ���룬�ͻ�����
'''
print (repr("���к�"))#'\xc0\xcf\xc4\xd0\xba\xa2' 6���ֽ�

'''һ��Ҫע����ǣ�
        #coding:GBK �����ļ��洢�ʹ򿪵�ʱ���Python2����Python3˵���Ǽ����Һ�Ͱ�����ԭ��Ĭ�ϵı���뷽ʽ����
                    GBK��ͬ��GBK�����UnicodeȻ���ڱ�������ܿ��������ģ������ǿ����ļ����ݺ���仰���������
                    ����������

                    Ȼ�������ڴ˿�ִ��print����ʱ����������ˣ��������Python2�У��������"���к�"����GBK�ֽ�
                    ����ʽ�����ڴ��еģ���Ҫ����Ϊ����2͵͵�İ�����Unicode������ֽڣ��������ִ�е�ʱ������Ҫ��
                    "���к�"����ֽڴ��ڱ�Ϊ�����ܿ��������ģ���ģ����ʱ��pycharm��cmd������һ�ţ���������˵��
                    Ҫ��ô������������ܿ��������ģ�����˵���㣬Ȼ��pycharm˵���Ӿ���utf-8������Unicode��
                    cmd˵���Ӿ���GBK������Unicode��֪������������������һ���������

                    GUI����������������������˸��ģ���Python3�У����ж���Unicode���Ǵ��������"���к�"����
                    Unicode�ֽڣ���Ϊ�����ھ����ڴ��У����ˣ�����Ҫִ������һִ�У��ֵô��ֽڱ�Ϊ���ģ��������
                    ʱ����Ҫ��������pycharm����cmd��Ϊ������Unicode�������Լ����ܱ������
'''

# print(u"hello"+"yuanhao")
# print (u"Ԭ��"+u"��˧")
# print (u"Ԭ��"+"��˧")