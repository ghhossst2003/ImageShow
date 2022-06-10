# coding=utf-8

import logging
from logging.handlers import TimedRotatingFileHandler
import time


def loggin_init(filename1):
    logger = logging.getLogger()
    # logfile = TimedRotatingFileHandler(filename=filename1, when='M', interval=1)
    # logfile.suffix = "%Y-%m-%d %H-%M-%S.log"
    logfile = TimedRotatingFileHandler(filename=filename1, when='H', interval=1)
    logfile.suffix = "%Y-%m-%d %H.log"
    formatter = logging.Formatter(
        '%(asctime)s  [%(filename)s %(lineno)d] : %(levelname)s  %(message)s')
    logfile.setFormatter(formatter)
    logfile.setLevel(logging.DEBUG)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,
                        handlers=(logfile, console))
    # logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    loggin_init('test')
    while True:
        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')
        time.sleep(10)
