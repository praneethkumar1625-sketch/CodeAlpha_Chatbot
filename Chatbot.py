def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"
    
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thanks for asking!"
    
    elif user_input in ["what is your name", "what's your name"]:
        return "I'm CodeBot, your simple assistant!"
    
    elif user_input in ["what can you do", "help"]:
        return "I can chat with you! Try saying hello, asking how I am, or say bye."
    
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    
    else:
        return "I didn't understand that. Try saying 'help' to see what I can do!"


def main():
    print("=" * 40)
    print("     Welcome to CodeBot!")
    print("=" * 40)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.strip() == "":
            print("CodeBot: Please type something!")
            continue
        
        response = get_response(user_input)
        print(f"CodeBot: {response}")
        
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


main()
