'''
该PY文件用于测试模块使用
'''

from common.custom_logger import CreateLogger

if __name__ == '__main__':

    #测试custom_logger（日志程序）
    logger = CreateLogger.get_logging().logger
    logger.error('日志程序测试！')