import os

my_local_file = os.path.join(os.path.dirname(__file__), 'my_file.txt')

with open(my_local_file) as file:
    content = file.read()
    print(content)
