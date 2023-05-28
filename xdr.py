#!/usr/bin/python3

# XDR Module

import xdrlib

###############################################
###               XDR ENCODE                ###
###############################################


def encode_double(val) -> bytes:
    """
    >>> encode_double(1.2).hex()
    '3ff3333333333333'
    """
    p = xdrlib.Packer()
    try:
        p.pack_double(val)
    except:
        print("packing the double failed!")
    data = p.get_buffer()
    # todo
    return data


def encode_int(val) -> bytes:
    """
    >>> encode_int(-1).hex()
    'ffffffff'
    """
    p = xdrlib.Packer()
    try:
        p.pack_int(val)
    except:
        print("packing the int failed!")
    data = p.get_buffer()
    # todo
    return data


def encode_uint(val) -> bytes:
    """
    >>> encode_uint(10).hex()
    '0000000a'
    """
    p = xdrlib.Packer()
    try:
        p.pack_uint(val)
    except:
        print("packing the uint failed!")
    data = p.get_buffer()
    # todo
    return data


def encode_bool(val: bool) -> bytes:
    """
    >>> encode_bool(True).hex()
    '00000001'
    """
    p = xdrlib.Packer()
    try:
        p.pack_bool(val)
    except:
        print("packing the bool failed!")
    data = p.get_buffer()
    # todo
    return data


def encode_string(val: str) -> bytes:
    """
    >>> encode_string("hello").hex()
    '0000000568656c6c6f000000'
    """
    p = xdrlib.Packer()
    try:
        p.pack_string(val.encode("utf-8"))
    except:
        print("packing the string failed!")
    data = p.get_buffer()
    # todo
    return data


def encode_two_int(val1, val2) -> bytes:
    """
    >>> encode_two_int(-1,2).hex()
    'ffffffff00000002'
    """
    p = xdrlib.Packer()
    try:
        p.pack_farray(2, [val1, val2], p.pack_int)
    except:
        print("packing the two int failed!")
    data = p.get_buffer()
    # todo
    return data

###############################################
###             XDR DECODE                  ###
###############################################


def decode_double(data: bytes):
    """
    >>> msg = bytes.fromhex('3ff3333333333333')
    >>> decode_double(msg)
    1.2
    """
    p = xdrlib.Unpacker(data)
    try:
        print(p.unpack_double())
    except:
        print("unpacking double failed!")
    return None


def decode_int(data: bytes):
    """
    >>> msg = bytes.fromhex('ffffffff')
    >>> decode_int(msg)
    -1
    """
    p = xdrlib.Unpacker(data)
    try:
        print(p.unpack_int())
    except:
        print("unpacking int failed!")
    return None


def decode_uint(data: bytes):
    """
    >>> msg = bytes.fromhex('00000001')
    >>> decode_uint(msg)
    1
    """
    p = xdrlib.Unpacker(data)
    try:
        print(p.unpack_uint())
    except:
        print("unpacking uint failed!")
    # todo
    return None


def decode_bool(data: bytes):
    """
    >>> msg = bytes.fromhex('00000001')
    >>> decode_bool(msg)
    True
    """
    p = xdrlib.Unpacker(data)
    try:
        print(p.unpack_bool())
    except:
        print("unpacking bool failed!")
    # todo
    return None


def decode_string(data: bytes) -> str:
    """
    >>> msg = bytes.fromhex('0000000568656c6c6f000000')
    >>> decode_string(msg)
    'hello'
    """
    p = xdrlib.Unpacker(data)
    try:
        data = p.unpack_string()
        data = data.decode("utf-8")
        print("'", data, "'", sep='')
    except:
        print("unpacking string failed!")
    # todo
    return None


def decode_two_int(data):
    """
    >>> msg = bytes.fromhex('ffffffff00000002')
    >>> decode_two_int(msg)
    (-1, 2)
    """
    p = xdrlib.Unpacker(data)
    try:
        val1 = p.unpack_int()
        val2 = p.unpack_int()
        print('(', val1, ', ', val2, ')', sep='')
    except:
        print("unpacking two int failed!")
    # todo
    return None


###############################################
###                MAIN                     ###
###############################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
