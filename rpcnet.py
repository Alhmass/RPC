#!/usr/bin/python3

# RPC Net Module

import socket
from rpcmsg import *

###############################################
###               CONSTANTS                 ###
###############################################

MAXMSG = 1500

###############################################
###                CALL UDP                 ###
###############################################


def call(host, port, xid, prog, vers, proc, args) -> bytes:
    result = b''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = encode_call(xid, prog, vers, proc, args)
    sock.sendto(msg, (host, port))
    response, address = sock.recvfrom(1500)
    rxid, data = decode_reply(response)
    if rxid != xid:
        raise Exception("[error] xid values are not the same")
    sock.close()
    return data

###############################################
###               REPLY UDP                 ###
###############################################


def reply(sserver, handle):
    msg, address = sserver.recvfrom(1500)
    xid, prog, vers, proc, args = decode_call(msg)
    data = handle(xid, prog, vers, proc, args)
    response = encode_reply(xid, data)
    sserver.sendto(response, address)
    return
