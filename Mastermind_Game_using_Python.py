import random

num=random.randrange(1000,10000)

n=int(input("Guess the 4 digits number:\n"))

if n==num:
    print("Great you have just guessed in single try! you're mastermind!")
    
else:
    ctrl=0
    
    while(n!=num):
        ctrl+=1
        count=0
        n=str(n)
        num=str(num)
        
        correct=["x"]*4
        
        for i in range(0,4):
            if n[i]==num[i]:
                count+=1
                correct[i]=n[i]
            else:
                continue
        print("Not quite the number.But you did get",count,"digit(s) correct!")
        print("\n\n")
        
        n=int(input("Enter your next choice of numbers:\n"))
        
        if count==0:
            print("None of your inouts match")
            n=int(input("Enetr your choice again"))
            
if n==num:
            ctrl+=1
            print("You are an mastermind")
            print("It took only",ctrl,"tries.")