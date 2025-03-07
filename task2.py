import random
def title():
    print('Welcome to Coin Toss \nIn this game you need guess heads or tails \n\n')
def game():
    while True:
        try:
           a=input('Please enter head or tail:')
           if a not in ['head','tail']:
              print('NO,Please enter "head" or "tail"')
              continue
           result=random.choice(['head','tail'])
           print(f'The result is {result}')
           if a == result:
             print('You win!')
           else:
             print('You lost, try again')
        except:
            print('No')


            
if __name__=='__main__':
    title()
    game()