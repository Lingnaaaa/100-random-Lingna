import random

def roll3():
    rolls=[]
    for _ in range(3):
        roll = random.randint(1,6)
        if roll==1:
            roll = random.randint(1,6)
        rolls.append(roll)
    return sum(rolls)
def roll4():
    rolls=[random.randint(1,6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)
print('Welcome to Advanced Dungeons and Dragons ')

print ("Charater stats (Rolling 3 , recolling 1s):")
for stat in ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma']:
    print(f"{stat}:{roll3()}")

print ("Charater stats (Rolling 4, dropping lowest): ")
for stat in ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma']:
    print(f"{stat}:{roll4()}")

