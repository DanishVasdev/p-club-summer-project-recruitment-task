import hashlib
import time

def find_x(s):
    a=hashlib.sha256()
    a.update(s.encode('utf-8'))
    hx=int(a.hexdigest(),16)
    target=int("0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",16)
    if(hx<=target):
             print("fine as it is")
    else:
        x=1
        while(1):
            t=s
            s=s+str(x)
            a=hashlib.sha256()
            a.update(s.encode('utf-8'))
            hx=int(a.hexdigest(),16)
            if(hx>target):
                x+=1
                s=t
            else:
                
                return x

t0= time.process_time()
inp=input("ENTER STRING:")
print(find_x(inp))
t1=time.process_time()
print("TIme elasped:",t1-t0)
