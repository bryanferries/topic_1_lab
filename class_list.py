classes = []    # Create an empty list

print()
print('******************************************************')
print('List all the classes you\'re taking this semester')
print('******************************************************')
print()

while True:     # Set up a while loop
    class_name = input('Enter name of class, or just press ENTER if finished ')  # Define class_name variable by soliciting input
    classes.append(class_name)      # and append that input to the classes list
    if class_name == '':        # If the user doesn't enter any input, break the while loop
        break

print()
print('[ CLASS LIST ]')
for class_name in classes:      # Loop over the classes list and print each item
    print(class_name)
