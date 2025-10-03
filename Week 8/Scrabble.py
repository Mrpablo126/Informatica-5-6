import random 
def main(words):
    dictionary = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    
    print("Welcome to Scrabble")
    print("Your letters are:")
   
def words_in_Scrabble(dictionary, words):
    words = random.randint(dictionary,13)
    print(words)
    words_in_Scrabble(dictionary,words)

main()