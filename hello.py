import os

def greet(name):
    print("Hello, " + name)

def run_cmd(cmd):
    os.system(cmd)   # 故意留一个命令注入风险点

# test greet
greet("world")
