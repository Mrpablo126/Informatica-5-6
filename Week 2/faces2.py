def main():
    emoji = input("Write a message with an emoticon:")
    print(convert(emoji))

def convert(message):

    message = message.replace(":)", "😊").replace(":(","😔").replace(":","Adriana salte 🗣️🗣️🗣️🗣️🗣️")
    
    return (message)
main()