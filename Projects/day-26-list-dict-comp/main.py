student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_phon = {}
with open("Projects/day-26-list-dict-comp/nato_phonetic_alphabet.csv") as f:
    dict_phon = {line.split(",")[0].strip("\n"):line.split(",")[1].strip("\n") for line in f}
    # for line in f:
    #     print(line.split(","))
    #     (key, val) = line.split(",")
    #     if key != "letter":
    #         dict_phon[key.strip("\n")] = val.strip("\n")

print(dict_phon)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_name = "Guilherme"
list_phon = [dict_phon[i.upper()] for i in list(input_name)]
print(list_phon)

