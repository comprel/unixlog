# coding:utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

from client.unix_client import LoggerClient


if __name__ == "__main__":
    c = LoggerClient()
    c.info("test", "xxx")
