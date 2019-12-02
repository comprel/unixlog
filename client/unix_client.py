# coding=utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

import socket
import sys
from base.format import to_str
from base.trace import findCaller
from conf import socket_file


class LoggerClient(object):
    def __init__(self):
        self.sock = None

    def __del__(self):
        if self.sock is not None:
            self.sock.close()

    def _init_socket(self):
        if self.sock is None:
            self.sock = self._set_socket()

        return self.sock

    def _set_socket(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        if sock < 0:
            print(sys.stderr, 'socket error')
        try:
            sock.connect(socket_file)
        except socket.error, msg:
            print(sys.stderr, "exception")
            print(sys.stderr, msg)
            sys.exit(1)

        return sock

    def _log(self, leavel, msg, *args, **kwargs):
        sock = self._init_socket()
        _tmp = to_str(msg)
        if args:
            for _args in args:
                _tmp += " " + to_str(_args)
        if kwargs:
            for key, value in kwargs.items():
                _tmp += " %s:" % key + to_str(value)
        filename, line = findCaller()
        _msg = '''[%s-L%s][ %s ] %s''' % (filename, line, leavel, _tmp)
        sock.sendall(_msg)

    def info(self, msg, *args, **kwargs):
        self._log("INFO", msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._log("ERROR", msg, *args, **kwargs)

