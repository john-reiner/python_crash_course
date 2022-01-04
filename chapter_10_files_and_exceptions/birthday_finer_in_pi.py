file_path = 'pi_digits_million.txt'

with open(file_path) as pi_object:
    lines = pi_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()


birthday = input("Please enter your bithday (mmddyy) to search: ")

if birthday in pi_string:
    print("Your bithday is in the first million digits of pi!")
else:
    print("Nope!")