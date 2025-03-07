def title():
    print('Number Guessing Game\nInstruction : AI will give you a inter number that round of 1-10\nYou need to enter a number')
    print('If the enter number is same as the number that AI give to you, then you win this game')
    print('Let\'s start it!\n ')


def game():
   import random
   a = round(random.uniform(1,100))
   counts=0
   while True:
      try:
         guess=input('Enter an integer between 1-100:')
         guess=int(guess)
         counts+=1
         if guess<1 or guess>100:
            print("Please enter a number between 1-100")
         if guess > a:
            print('Try a samller number')
         if guess < a:
            print('Try a larger number')
         if guess == a:
            print(f'Congratulations! You win! You took {counts} time to got the answer is {a}')
            break
      except:
         print('Enter a integer number')
         
         
      
   
if __name__=="__main__":
 title()
 game()

