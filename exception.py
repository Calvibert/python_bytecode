
# import dis
# exec(open("exception.py").read())
# #Exception thrown
# dis.distb()
# #Shows the line in bytecode where the exception occurs

1/0

'''  5           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (0)
    -->       4 BINARY_TRUE_DIVIDE
              6 POP_TOP
              8 LOAD_CONST               2 (None)
             10 RETURN_VALUE
'''