import greet_random as a
quit_msg=["see you soon!!","You can use me whenever you are in need!!"]
greetings=a.greet_random()
print(greetings,",","Iam a WORDBOT!!!i can make your calculations EASIER and FASTER")
dictn={'Easy':'Simple','Good': 'fine','Small': 'tiny','Big': 'large'}
while True:
    msg=input()
    if msg in quit_msg:
        break
    else:
        print('The meaning of {} is {}'.format(msg, dictn[msg]))
           