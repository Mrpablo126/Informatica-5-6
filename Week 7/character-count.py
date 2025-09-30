#Esta mugre es capas de contar caracteres y decir la cantidad de veces que aparece la letra.
def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1

    print(dictionary)
    print(dictionary(len[character]))
message = input("Write a messege:")
dictionary = {}
character_counter(message, dictionary)
