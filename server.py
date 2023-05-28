#!/usr/bin/python3

# RPC Server (UDP)

import sys
import socket
import xdr
import rpcnet
import rpcmsg
import rpcbind

###############################################
###              CONSTANTS                  ###
###############################################

TEST_PROG = 0x20000001
TEST_VERS = 1

PROC_NULL = 0
PROC_PI = 1
PROC_INC = 2
PROC_ADD = 3
PROC_ECHO = 4

###############################################
###             PROCEDURE                   ###
###############################################


def null() -> bytes:
    return null


def pi() -> bytes:
    return xdr.encode_double(3.1415926)


def inc(x: int) -> bytes:
    return xdr.encode_int(x + 1)


def add(x: int, y: int) -> bytes:
    return xdr.encode_int(x + y)


def echo(s: str) -> bytes:
    return xdr.encode_string(s)


def handle(xid, prog, vers, proc, args):
    if prog != TEST_PROG:
        raise Exception("Error the prog call is not the actual program")
    if vers != TEST_VERS:
        raise Exception("Error the vers is not the actual running version")
    if proc == PROC_NULL:
        return null()
    elif proc == PROC_PI:
        return pi()
    elif proc == PROC_INC:
        x = xdr.decode_uint(args)
        return inc(x)
    elif proc == PROC_ADD:
        x, y = xdr.decode_two_int(args)
        return add(x, y)
    elif proc == PROC_ECHO:
        s = xdr.decode_string(args)
        return echo(s)
    else:
        return null()

###############################################
###                 MAIN                    ###
###############################################


if (len(sys.argv) != 2):
    print("Usage: server.py <port>")
    sys.exit(1)

host = ''
port = int(sys.argv[1])
status = rpcbind.register(1000, TEST_PROG, TEST_VERS, port)
if status == False:
    raise Exception("Error the register method failed!")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while (True):
    rpcnet.reply(s, handle)

s.close()
