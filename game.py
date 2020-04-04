import random
p = int(input("enter the box size\n"))
game = int(input("for ai vs ai enter 2 for ai vs human enter 1\n"))
print("select a number in between o,1 for toss")
toss = int(input("enter the number\n"))
if toss != 0 or 1:
    print("select eithe 0 or 1\n")
lis = [0,1]
lis = random.choice(lis) 
print(lis)
while(p!=0 and game == 1):
    if lis == toss:
        print(p)
        man = int(input("enter the number of sticks"))
       
        if man == 1 or 2 or 3:
            p = p - man
            print("the numof sticks",p)
            if p ==0:
                print("u have lost the game")
                break
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-2
            print("computer has selected",2)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("user has won")
                break
            else:
                print("computer has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("user has won")
            break
    if lis != toss:
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-2
            print("computer has selected",2)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("user has won")
                break
            else:
                print("computer has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("user has won")
            break
        print(p)
        man = int(input("enter the number of sticks"))
       
        if man == 1 or 2 or 3:
            p = p - man
            print("the numof sticks",p)
            if p ==0:
                print("u have lost the game")
                break
while(p!=0 and game == 2):
    if lis == toss:
        print(p)
        print("ai1 ha won the toss")
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer1 has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer1 has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-2
            print("computer1 has selected",2)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("ai has won")
                break
            else:
                print("computer1 has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("ai has won")
            break          
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer2 has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer2 has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-3
            print("computer2 has selected",3)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("ai2 has won")
                break
            else:
                print("computer2 has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("ai2 has won")
            break        
    if lis != toss:
        print(p)
        print("ai2 ha won the toss")
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer2 has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer2 has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-2
            print("computer2 has selected",3)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("ai2 has won")
                break
            else:
                print("computer2 has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("ai2 has won")
            break 
        if(p%3 == 1 and p%2 != 1 and p > 3):
            p=p-3
            print("computer1 has selected",3)


        elif(p%3 != 1 and p%2 == 1 and p > 2):
            p=p-2
            print("computer1 has selected",2)
        elif(p%3 == 1 and p%2 == 1 and p > 3):
            p=p-2
            print("computer1 has selected",2)
        elif(p%3 != 1 and p%2 != 1):
            p=p-1
            if(p==0):
                print("ai has won")
                break
            else:
                print("computer1 has selected",1)
        elif(p%3 == 1 and p%2 == 1 and p == 1):
            print("ai2 has won")
            break