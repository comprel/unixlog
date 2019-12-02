# coding:utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

from server.unix_socket import UnixSocketChannel


if __name__ == "__main__":
    try:
        UnixSocketChannel().listener()
    except KeyboardInterrupt as e:
        print("socket shutdown, bye bye ...")

