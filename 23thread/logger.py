# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description:
"""
import logging


def get_logger(name, log_file=None, log_level='DEBUG'):
    """
    logger
    :param name: 模块名称
    :param log_file: 日志文件，如无则输出到标准输出
    :param log_level: 日志级别
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level.upper())
    formatter = logging.Formatter(
        '[%(levelname)7s %(asctime)s %(processName)s %(threadName)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%Y%m%d %I:%M:%S')
    if log_file:
        f_handle = logging.FileHandler(log_file)
        f_handle.setFormatter(formatter)
        logger.addHandler(f_handle)
    handle = logging.StreamHandler()
    handle.setFormatter(formatter)
    logger.addHandler(handle)
    return logger


logger = get_logger(__name__, log_file=None, log_level='DEBUG')


def set_log_level(log_level='INFO'):
    logger.setLevel(log_level.upper())


if __name__ == '__main__':
    logger.debug('hi')
    logger.info('hi')
    logger.error('hi')
    logger.warning('hi')
    set_log_level('info')
    logger.debug('hi')  # ignore
    logger.info('hi')
    logger.error('hi')
    logger.warning('hi')
    import threading
    import time


    def doubler(number, logger):
        logger.info("aaaa")
        logger.warning("bbbb")
        logger.error("cccc")

        result = number * 2
        time.sleep(5)
        logger.info('result: {}'.format(result))


    thread_names = ['Mike', 'George', 'Wanda']
    # logger = get_logger('test_thread')
    for i in range(3):
        my_thread = threading.Thread(
            target=doubler, name=thread_names[i], args=(i, logger))
        my_thread.start()
