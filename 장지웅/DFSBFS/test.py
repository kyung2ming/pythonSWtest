import time
import sys
import path
import os

start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q1_input1.txt","r")

# 이렇게 아래처럼 사용하면 2차원 배열 생성 가능


data = f.readlines()
for i in range(len(data)) :
    data[i] = data[i].strip().split()  

f.close()
data = data[1:]
print(data)