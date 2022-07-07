#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#from email import contentmanager


from email.mime import base


with open("Projects/day-24-file-system/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    base_content = file.read()
    

with open("Projects/day-24-file-system/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.read()
    # could use names = file.readlines() instead so wouldnt need to use split ("\n")
    # but using this method it is needed to strip \n from the lines

list_names = names.split("\n")
#print(list_names)
for name in list_names:
    write_content = base_content.replace("[name]",name)
    with open(f"Projects/day-24-file-system/Mail Merge Project Start/Output/Letter to {name}.txt", mode="w") as file_write:
        file_write.write(write_content)