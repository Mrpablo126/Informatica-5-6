#Esta mugre es capas de contar caracteres y decir la cantidad de veces que aparece la letra.
def main():
    def character_counter(message, dictionary):
        for character in message:
            dictionary.setdefault(character, 0)
            dictionary[character] += 1

        print(dictionary)
        
    message = input("Write a message:")
    dictionary = {}
    character_counter(message, dictionary)

    print(f"The number of characters in the message is:{len(message)}")
main()