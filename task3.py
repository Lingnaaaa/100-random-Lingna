import random
def title():
    print('Welcome Rock Paper Scissors Game')

def game():
    while True:
        try:
            a=input('Please enter R or P or S:')
            if a not in ['R','P','S']:
              print('NO,Please enter "R" or "P" or "S"')
              continue
            result=random.choice(['R','P','S'])
            print(f'The result is {result}')
            if a =='R' and result!='P':
                print('You Win!')
                #break
            if a =='R' and result=='P':
                print('You lost')
            if a =='P' and result !='S':
                print('You win!')
                #break
            if a =='P' and result =='S':
                print('You lost')
            if a =='S' and result !='R':
                print('You Win!')
            if a =='S' and result =='R':
                print('You lost')
        except:
            print('No')

if __name__=='__main__':
    title()
    game()
    
