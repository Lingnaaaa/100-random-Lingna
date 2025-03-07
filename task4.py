import random
def title():
    print('Welcome to Dungeons and Dragons Character Generator')
    print('In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.')
    #strength intelligence wisdom dexterity constitution charisma

def game():
    while True: 
        result1=random.choice(['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma'])
        result2=random.choice(['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma'])
        result3=random.choice(['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma'])
        print(f'You character is have {result1},{result2},{result3} ')
        break

if __name__=='__main__':
    title()
    game()
        
        

    