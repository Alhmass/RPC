#!/usr/bin/python3

# RPC Message Module

import xdrlib

###############################################
###             RPC CONSTANTS               ###
###############################################

CALL = 0
REPLY = 1
RPC_VERSION = 2
AUTH_NONE = 0
MSG_ACCEPTED = 0
MSG_DENIED = 1
SUCCESS = 0

###############################################
###             ENCODE CALL                 ###
###############################################


def encode_call(xid, prog, vers, proc, data) -> bytes:
    """
    >>> encode_call(1, 1, 1, 1, b'ABCD').hex()
    '0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344'
    """
    p = xdrlib.Packer()
    try:
        p.pack_uint(xid)
        p.pack_uint(CALL)
        p.pack_uint(RPC_VERSION)
        p.pack_uint(prog)
        p.pack_uint(vers)
        p.pack_uint(proc)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(AUTH_NONE)
        p.pack_fstring(len(data), data)
    except:
        print("packing the string failed!")
    msg = p.get_buffer()
    # todo
    return msg

###############################################
###             ENCODE REPLY                ###
###############################################


def encode_reply(xid, data) -> bytes:
    """
    >>> encode_reply(1, b'ABCD').hex()
    '00000001000000010000000000000000000000000000000041424344'
    """
    p = xdrlib.Packer()
    try:
        p.pack_uint(xid)
        p.pack_uint(REPLY)
        p.pack_uint(MSG_ACCEPTED)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(SUCCESS)
        p.pack_fstring(len(data), data)
    except:
        print("packing the string failed!")
    msg = p.get_buffer()
    # todo
    return msg

###############################################
###            DECODE CALL                  ###
###############################################


def decode_call(msg: bytes):
    """
    >>> msg = bytes.fromhex('0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344')
    >>> decode_call(msg)
    (1, 1, 1, 1, b'ABCD')
    """
    data = msg[40:]
    p = xdrlib.Unpacker(msg)
    xid = prog = vers = proc = 0
    try:
        xid = p.unpack_uint()
        _ = p.unpack_uint()
        _ = p.unpack_uint()
        prog = p.unpack_uint()
        vers = p.unpack_uint()
        proc = p.unpack_uint()
    except:
        print("unpacking failed!")
    return (xid, prog, vers, proc, data)

###############################################
###             DECODE REPLY                ###
###############################################


def decode_reply(msg):
    """
    >>> msg = bytes.fromhex('00000001000000010000000000000000000000000000000041424344')
    >>> decode_reply(msg)
    (1, b'ABCD')
    """
    xid = 0
    data = msg[24:]
    p = xdrlib.Unpacker(msg)
    try:
        xid = p.unpack_uint()
    except:
        print("unpacking failed!")
    return (xid, data)

###############################################
###                MAIN                     ###
###############################################


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
