# coding=utf8

import logging
import logging.config
import logging.handlers
from conf import default_log
from conf import log_leavel

levelmap = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


class LogSetup(object):
    def __init__(self, name, keep=None):
        self.name = name
        self.keep = keep
        self.setup()

    def setup(self):
        if self.keep:
            handler = logging.handlers.RotatingFileHandler(filename=self.name,
                                                           maxBytes=500 * 1024 * 1024,
                                                           backupCount=3)
        else:
            handler = logging.handlers.TimedRotatingFileHandler(filename=self.name, when='midnight', backupCount=7)
            logging.getLogger(self.name).setLevel(levelmap.get(log_leavel, logging.INFO))
        formatter = logging.Formatter("[%(asctime)s] %(message)s")
        handler.setFormatter(formatter)
        logging.getLogger(self.name).addHandler(handler)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        logging.getLogger(self.name).addHandler(consoleHandler)


def get_logger(name=None, keep=None):
    if name == '' or not name:
        name = default_log or "/tmp/unixLogService.log"
    LogSetup(name=name, keep=keep)
    return logging.getLogger(name)

