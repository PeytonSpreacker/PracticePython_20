import random

# boolean logic
def boolean():
    while True:
        # generate a random list of 5 numbers between 1 and 10
        lst = random.sample(range(1,11),5)
        # print(lst)
        check = input('Pick a number between one and 10: ')
        if check == 'quit':
            quit()
        else:
            num_check = int(check)
        if num_check in lst:
            print(num_check, 'is in the list.')
        else:
            print(num_check, 'is not in the list.')

# equality testing
def vote_age():
    age = int(input('How old are you? '))
    if age == 18 or age > 18:
        print('Congrats! You can now vote!')
    else:
        print('You cannot vote yet.')

# binary search

# boolean()
vote_age()