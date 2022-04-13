alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
def encrypt(text,shift):
    original_text_list = list(text)
    original_text_pos = []
    for letter in original_text_list:
        original_text_pos.append(alphabet.index(letter))
    # print(original_text_pos)
    cyphered_text_pos = []
    for x in original_text_pos:
        #print(f"Start... x={x}")
        if int(x)+int(shift) > 25:
            plus_remainder = int(x)+int(shift)-26
        else:
            plus_remainder = int(x)+int(shift)
        #print(f"End... plus={plus_remainder}")
        cyphered_text_pos.append(int(plus_remainder))
    # print(cyphered_text_pos)
    cyphered_text = []
    for i in cyphered_text_pos:
        cyphered_text.append(alphabet[i])
    print(f"The encoded text is {''.join(cyphered_text)}")

def decrypt(text, shift):
    encrypted_text_list = list(text)
    encrypted_text_pos = []
    for letter in encrypted_text_list:
        encrypted_text_pos.append(alphabet.index(letter))
    
    decrypted_text_pos = []
    # print(encrypted_text_pos)
    for y in encrypted_text_pos:
        if int(y)-int(shift) < 0:
            minus_remainder = int(y)-int(shift)+26
        else:
            minus_remainder = int(y)-int(shift)        
        decrypted_text_pos.append(int(minus_remainder))
    # print(decrypted_text_pos)
    decrypted_text = []
    for i in decrypted_text_pos:
        decrypted_text.append(alphabet[i])
    print(f"The decoded text is {''.join(decrypted_text)}")


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Please type encode or decode.")
