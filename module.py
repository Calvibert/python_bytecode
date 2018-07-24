#
def hello(value):
    returnVal = value
    if returnVal > 1:
        return returnVal

print(hello.__code__)
print(hello.__code__.co_consts)
print(hello.__code__.co_varnames)
print(hello.__code__.co_code)

print(ord('|'))
import dis
print(dis.opname[124])

print(dis.dis(hello))

print(dis.dis(hello))