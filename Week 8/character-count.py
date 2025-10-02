#Esta mugre es capas de contar caracteres y decir la cantidad de veces que aparece la letra.
def main():
    def character_counter(message, dictionary):
        for character in message:
            dictionary.setdefault(character, 0)
            dictionary[character] += 1

        print(dictionary)
        values_list = list(dictionary.values())
        print(values_list)
        largest_number_index = values_list.index(max(values_list))
        repeated_character = list(dictionary.keys())[largest_number_index]
        print(f"The most repeteated character is: {repeated_character}, repeating {dictionary[repeated_character]}")

        # print(sum(dictionary.values())) es lo mismo que la linea 21
        #Alternativa 2
        largest_number2 = max(dictionary, key=dictionary.get)
        print(f"The most repeteated character is:{largest_number2}, repeating {dictionary[repeated_character]}")
        
    message = input("Write a message:")
    dictionary = {}
    character_counter(message, dictionary)

    print(f"The number of characters in the message is:{len(message)}")
main()