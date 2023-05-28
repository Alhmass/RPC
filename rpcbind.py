#!/usr/bin/python3

# RPC Bind Module

import xdrlib
import xdr
import rpcnet
import rpcmsg

###############################################
###           CONSTANTS                     ###
###############################################

RPCB_HOST = "localhost"
RPCB_PORT = 111
RPCB_PROG = 100000  # rpcbind / portmap
RPCB_VERS = 4

RPCBPROC_SET = 1
RPCBPROC_UNSET = 2
RPCBPROC_GETADDR = 3

###############################################
###                GETPORT                  ###
###############################################


def getport(xid, prog, vers) -> int:
    port = -1
    args = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string(
        "udp") + xdr.encode_string("") + xdr.encode_string("")
    reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG,
                        RPCB_VERS, RPCBPROC_GETADDR, args)
    data = xdr.decode_string(reply)
    port_str = data.split('.')[4:]
    port = int(port_str[0]) * 256 + int(port_str[1])
    return port


###############################################
###                 REGISTER                ###
###############################################

def register(xid, prog, vers, port) -> bool:
    args = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string(
        "udp") + xdr.encode_string("") + xdr.encode_string("")
    reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid,
                        RPCB_PROG, RPCB_VERS, RPCBPROC_SET, args)
    return xdr.decode_bool(reply)

###############################################
###              UNREGISTER                 ###
###############################################


def unregister(xid, prog, vers) -> bool:
    port = -1
    args = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string(
        "udp") + xdr.encode_string("") + xdr.encode_string("")
    reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG,
                        RPCB_VERS, RPCBPROC_UNSET, args)
    return xdr.decode_bool(reply)
