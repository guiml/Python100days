sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


# You are going to use Dictionary Comprehension to create a dictionary called result that takes 
# each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop

# Don't change code above 👆

# Write your code below:

result = {i:len(i) for i in sentence.split()}

print(result)