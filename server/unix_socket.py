# coding:utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import socket
import sys
from base.logs import logger
from conf import socket_file


class UnixSocketChannel(object):
    def _set_socket(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        if sock < 0:
            print (sys.stderr, 'socket error')
            sys.exit(1)

        if os.path.exists(socket_file):
            os.unlink(socket_file)
        if sock.bind(socket_file):
            print (sys.stderr, 'socket.bind error')

        return sock

    def listener(self):
        sock = self._set_socket()
        print (sys.stderr, 'listener started, wait connecting ...')
        while True:
            try:
                while True:
                    data = sock.recv(81920)
                    if data:
                        logger.info(data)
                    else:
                        break
            except Exception as e:
                logger.info(e)
