'''
This Code tells us that whether the number is equal to 18 or not and 
you have 9 guesses to guess the correct number.
'''

n = 18

i = 1

while i <= 9:
    x = int(input())
    if x == n:
        print("Congrats! You got the Right number.")
        break
    else:
        if x > n:
            print ("Guess the smaller number.")
        else:
            print ("Guess a larger Number.")

        print ("No. of guesses left :- " , 9 - i)
        i += 1



print ("Game Over.")
