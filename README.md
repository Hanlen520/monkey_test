V2.1 2017/08/08

1.�����ֶ����Թ�������������ͳ��
2.monkeyTest.py��line72~line131 Ϊ�ֶ����Բ���
3.monkeyTest.py��line134~line191ΪMonkey���Բ���
4.ע�����ֲ��Կ�ʼ����ע�ͣ�����ע�����ݽ�����ش������


V2.0  2017/08/07

1.�Ż���ͳ���������ݵĴ���,��Ҫ��cpu rate�ļ��㷽ʽ
2.������豸����ͳ�ƴ������⣬ʹ�ó־û���¼������Ϣ
3.���ձ����ʽ�޸�



V1.5
1.����Config�����ļ�
2.�����豸ʵʱ��أ�֧����ʱ�Ͽ��豸���������豸��ÿ10s���һ���豸���Զ�����
3.����monkey_stop.py��֧����ʱֹͣmonkey���в����������������ɸ�����Ҫѡ���Ƿ�ִ�У�
4.������������ͳ�Ƽ��2s�����Զ��壩
5.�Ż���ɾ�����������ļ�������

# monkey �����ļ�Config.py
class Config:
    # apk����
    package_name = "com.quvideo.slideplus"
    # Ĭ���豸�б�
    device_dict = {}
    # ����
    net = "wifi"
    # monkey seedֵ���������
    monkey_seed = str(random.randrange(1, 1000))
    # monkey ����
    monkey_parameters = "--throttle 200 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 5000"
    # log�����ַ
    log_location = "D:\\PyCharm\\Monkey_performance\\log\\"
    #�������ݴ洢Ŀ¼
    info_path = "D:\\PyCharm\\Monkey_performance\\info\\"
    

����monkey���ԣ�ִ��monkeyTest.py
ֹͣ����monkey��ִ��monkey_stop.py
�����Ҫ�����豸����ִ��monkey_stop.pyǰ��ɾ��#reboot(dev,dev_model)ǰ��ע�ͼ���
    

V1.0
# monkey ѹ�����Լ�����ͳ��
* python3 
* ͳ��������Ϣcpu,men,fps,battery,flow
* ֧��wifi,gprsͳ��
* ͳ��crash��Ϣ
 
fpsͳ�ƣ�
��Ҫ�򿪿����������GPU����ģʽ����-��adb shell dumpsys gfxinfo��