import random

#value = random.randint(0, 100)
#result = value + 50
#print(result)

#RSS = random.choice(['Rock', 'Paper', 'Shoe'])

def main():
    print("Welcome to my rock paper scissors game!")

    inp = input("Type rock, paper, or scissor: ")
    
    if inp in ['rock','Rock']:
        rss1 = random.choice(['Rock', 'Paper', 'Scissor'])
        print(rss1)
        if rss1 == 'Paper':
            print("You lost")
        elif rss1 == 'Rock':
            print("Tie, try again")
        else:
            print("You won!")
    elif inp in ['paper','Paper']:
        rss2 = random.choice(['Rock', 'Paper', 'Scissor'])
        print(rss2)
        if rss2 == 'Scissor':
            print("You lost")
        elif rss2 == 'Paper':
            print("Tie, try again")
        else:
            print("You won!")
    elif inp in ['scissor', 'Scissor']:
        rss3 = random.choice(['Rock', 'Paper', 'Scissor'])
        print(rss3)
        if rss3 == 'Rock':
            print("You lost")
        if rss3 == 'Scissor':
            print("Tie, try again")
        else:
            print("You won!")
        
main()



