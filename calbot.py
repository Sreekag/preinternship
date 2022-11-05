import greet_random as g
import math
quit_msg=["see you soon!!","You can use me whenever you are in need!!"]
greetings=g.greet_random()
print(greetings,"Iam a CALBOT!!!i can make your calculations EASIER and FASTER")
while True:
    msg=input()
    if msg in quit_msg:
        break
    else:
        split_msg=msg.split()
        a1=float(split_msg[1])
        a2=float(split_msg[2])
        if 'add' in msg:
            print(n+m)
        if 'sub' in msg:
            print(n-m)
        if 'mul' in msg:
            print(n*m)
        if 'div' in msg:
            print(n/m)
        if 'pow' in msg:
            print(n**m)
        if 'sqr' in msg:
            print(math.sqrt(n))
        
    

