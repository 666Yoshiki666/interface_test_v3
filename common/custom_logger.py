'''
该PY文件用于生成日志程序
目录：
    BATH_PATH - 项目路径地址
    LOG_PATH - 日志存放地址
    InitializeLogger - 初始化日志程序的类
    CreateLogger - 生成日志程序的类
'''

import os
import logging
import threading
from datetime import datetime

'''
    os.path.dirname(file_path) #返回文件所在目录
    os.path.realpath(path) #返回path真实路径
    os.path.join(path,catalog) #路径拼接
'''

#项目路径
BATH_PATH = os.path.realpath(path='D://pycharm//interface_test_v3')
#日志路径
LOG_PATH = os.path.join(BATH_PATH, 'log')
#判断日志路径是否不存在，不存在即创建该目录
if not os.path.exists(path=LOG_PATH):
    os.mkdir(path=LOG_PATH)

'''
初始化日志程序的类
'''
class InitializeLogger:

    def __init__(self):
        #创建日志程序
        self.logger = logging.getLogger()
        '''
            logging模块定义的日志级别
                DEBUG #最详细的日志信息，典型应用场景是 问题诊断
                INFO #信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
                WARNING #当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
                ERROR #由于一个更严重的问题导致某些功能不能正常运行时记录的信息
                CRITICAL #当发生严重错误，导致应用程序不能继续运行时记录的信息
            日志等级：DEBUG < INFO < WARNING < ERROR < CRITICAL
            日志信息量：DEBUG > INFO > WARNING > ERROR > CRITICAL
        '''
        #设置日志等级
        self.logger.setLevel(level=logging.INFO)
        #创建日志记录文件
        handler = logging.FileHandler(filename=os.path.join(LOG_PATH, str(datetime.now().strftime('%Y%m%d') + '.log')))
        #创建格式化程序，即规范日志打印格式
        formatter = logging.Formatter(fmt='%(asctime)s => %(name)s => %(levelname)s => %(message)s', datefmt='%Y/%m/%d-%H:%M:%S')
        #日志文件设置打印格式
        handler.setFormatter(fmt=formatter)
        #日志程序设置日志文件样式
        self.logger.addHandler(hdlr=handler)

'''
调用初始化日志程序类，生成日志程序
'''
class CreateLogger:

    #日志程序
    logger = None
    #线程锁Lock
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_logging():
        if CreateLogger.logger is None:
            #CreateLogger类上锁
            CreateLogger.mutex.acquire()
            #生成日志程序
            CreateLogger.logger = InitializeLogger()
            #CreateLogger类释放锁
            CreateLogger.mutex.release()
        return CreateLogger.logger