import rpcbind

# register prog 0x30000001 (version 1) with port 4001
ret1 = rpcbind.register(1, 0x30000001, 1, 4001)
# register prog 0x30000002 (version 1) with port 4002
ret2 = rpcbind.register(2, 0x30000002, 1, 4002)
# unregister prog 0x30000002 (version 1)
ret3 = rpcbind.unregister(3, 0x30000002, 1)
# get port of program 0x30000001 (version 1)
port = rpcbind.getport(4, 0x30000001, 1)
print("port =", port)