""" This script is to generate a list of unique and random numbers (1 to 49) accordingly to numbers in each list(nums) and number of bets(list) which you want. 
The nums (numbers to be generated) in each list(bet) must be between 6 to 12.
There is no limit to the numbers of bets.""" 

#import random module to generate random numbers
import random

# define a quick pick function with nums(number of generated numbers) and bets(number of bets)
def quick_pick(nums, bets):
    # create a empty all_toto variable to store the list of generated numbers
    all_toto = [] 
    for bet in range(bets):
        one_toto = []
        while one_toto == []:
            for num in range(nums):
                # generate a random integral between 1 to 49
                rand_n = random.randint(1,49)
                one_toto.append(rand_n)
            
            # if there is any duplicate, it will reset
            if len(one_toto) != len(set(one_toto)):
                one_toto = []

        # if there is no duplicate, append it to the all_toto    
        else:
            all_toto.append(sorted(one_toto))
    
    # print each set of generated toto number per line for easy viewing
    for toto in all_toto:
        print(toto)


if __name__ == '__main__':
# Create a nums variable for user to input a number between 6 to 12.
# If the number is out of this range, it will keep asking the user to enter the correct number
    nums = int(input('Please enter number between 6 to 12: '))
    while nums < 6 or nums > 12:
        if nums < 6 or nums > 12:
            nums = int(input('Please enter ONLY number between 6 to 12: '))
        else:
            break
            
    bets = int(input('Please enter the number of bets: '))
    quick_pick(nums, bets)