import random 

secret_num=random.randint(1,10)
attempts=3
 
print("I'm thinking about a number between 1-10")
while attempts >0 :
    guess = int(input("take a guess?"))
    if guess == secret_num:
        print("congo!!!! you have guess the number correctly!")
        break
    elif guess > secret_num:
        print("the number is too high ")
        
    elif guess < secret_num:
        print("the  number is too low !!")
    attempts -= 1
if attempts==0:
    print("you don't have any attempt left !! and the secret number was",secret_num)
    
