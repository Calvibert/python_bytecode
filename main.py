import module
import dis

def call_hello():
    print(module.hello(2))


print(dis.dis(call_hello))