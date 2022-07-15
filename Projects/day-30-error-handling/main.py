from ssl import Purpose


list_num = [1,2,3]

try: 
    list_num[3]
except IndexError:
    print("List has no more than 3 keys")


try:
    erroneous_code
except NameError as error_msg:
    print(f"Error: {error_msg}")