# import os
# my_local_file = os.path.join(os.path.dirname(__file__), 'my_file.txt')

## ADD A NEW LINE
# with open(my_local_file, mode="a") as file:
#     file.write("\nNew text.")

# with open("Projects/day-24-file-system/new_file.txt", mode="w") as file:
#     file.write("\nNew text.")


with open("/Users/guilouzada/Documents/Data Eng/Python/data.txt") as file:
    content_file = file.read()
    print(content_file)
#     file.write("\nNew text.")


with open("../data.txt") as file:
    content_file = file.read()
    print(content_file)
#     file.write("\nNew text.")