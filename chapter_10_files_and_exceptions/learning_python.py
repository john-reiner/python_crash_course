file_path = 'learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    

string = ""

for line in lines:
    string += line.strip()

print(string.replace('Python', "Ruby"))