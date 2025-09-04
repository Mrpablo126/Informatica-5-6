def main():

    message = input("Write a messege:").lower() #This line is the message
    encode_message(message) #Is the where is the message

def encode_message (text): # Is defining the encode_message
    alphabet = "abcdefghijklmnopqrstuvwxyz" #Is the alphabet
    cipher =   "zyxwvutsrqponmlkjihgfedcba" #is the alphabet,but start from the z to the a
    new_message = "" #Nothing   
    i = 0 # is the counting
    
    while i < len(text): # The loop for the operation
        char = text[i] # For counting the characters of the word

        if char in alphabet: # This if protect the character and delete numbers or signs  
            cipher_index = alphabet.find(char) # This is going to find the character on the word
            new_message += cipher[cipher_index] # is the new messege 
        else:
            new_message += char # This is going to put the other things that are not on the alphabet out.
        i += 1 #Is going to find all the characters depending of the number of characters.
    print("Encoded message:" + new_message) #Is the print for the final result




main ()