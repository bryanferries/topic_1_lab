name = input('Enter your name ')
birth_month = input('enter your birth month ')
letters_in_name = len(name)     # Simple variables from input

print(f'Hello {name}.')  # Print message output using the f and {} for simplification
print(f'There are {letters_in_name} letters in your name.')

if birth_month == 'September':      # A simple conditional to print "Happy birthday month" if
    print('Happy birthday month!')  # the user entered "September" for their birth month.
else:
    print('Your birthday is not this month.')
