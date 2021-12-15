number01 = 8
number02 = 2
for i in range(10):
    number01+=number02
print(number01)#1

number01 = 2
print(number01)#2

number02 = number01**4
print(number02)#3

array1 = [0,0,0,0,0,0,1,1]
array2 = [1,0,0,0,1,1,1,0]
loop=0
out=[]
for i in range(len(array1)):
    if array1[loop] == array2[loop]:
        out.append(array1[loop])
    else:
        out.append(0)
    loop+=1
out=out[1:]
out.append(0)
outdata=""
loop=0
for i in range(len(out)):
    outdata+=str(out[loop])
    loop+=1
print(outdata)#4

outdata=""
loop=0
for i in range(len(out)):
    outdata=str(out[loop])+outdata
    loop+=1
print(outdata)#5

loop=0
for i in range(len(out)):
    outdata=str(out[loop])+outdata
    loop+=1

print(outdata)#6
