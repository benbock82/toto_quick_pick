""" This script is to generate a list of unique and random numbers (1 to 49) accordingly to numbers in each list(nums) and number of bets(list) which you want. 
The nums (numbers to be generated) in each list(bet) must be between 6 to 12.
There is no limit to the numbers of bets.""" 

#import random module to generate random numbers
import random
import time

# define a quick pick function with nums(number of generated numbers) and bets(number of bets)
def quick_pick(nums, bets):
    all_toto = []
    for num_set in range(bets):
        total_numbers = list(range(1, 50))
        random_bank = []
        for i in range(nums):
            random_one = random.choice(total_numbers)
            random_bank.append(random_one)
            total_numbers.remove(random_one)
        all_toto.append(sorted(random_bank))
    for toto in all_toto:
        print(toto)
    

if __name__ == '__main__':
# Create a nums variable for user to input a number between 6 to 12.
# If the number is out of this range, it will keep asking the user to enter the correct number
    print(f"Welcome to the lucky toto generator!\nYou are the lucky one.")
    nums = int(input('Please enter number between 6 to 12: '))
    while True:
        if nums < 6 or nums > 12:
            nums = int(input('Please enter ONLY number between 6 to 12: '))
        else:
            break
# Create a nums variable for user to enter numbers of bet (1 and above).
# If the number is condition, it will keep asking the user to enter the correct number             
    bets = int(input('Please enter the number of bets (1 and above): '))
    while True:
        if bets <= 0:
            bets = int(input('Please enter only number 1 and above: '))
        else: 
            break
    quick_pick(nums, bets)