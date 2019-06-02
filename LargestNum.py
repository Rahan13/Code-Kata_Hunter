a= input()
b = input().split()
b.sort()
i=len(b)-1
if(b.count('0') == len(b)):
    print(0)
else:
    while(i>=0):
        print(int(b[i]),end = "")
        i -= 1
