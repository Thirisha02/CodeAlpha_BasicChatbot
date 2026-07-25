# ==========================================
# CodeAlpha Python Internship
# Task 4 - Basic Chatbot
# Developed by: Thirisha J
# ==========================================

def show_commands():
    print("\nAvailable Commands:")
    print("- hi")
    print("- hello")
    print("- hey")
    print("- good morning")
    print("- good afternoon")
    print("- good evening")
    print("- good night")
    print("- how are you")
    print("- your name")
    print("- who created you")
    print("- help")
    print("- thanks")
    print("- bye")


def chatbot():
    print("=" * 50)
    print("🤖 Welcome to CodeAlpha Smart Chatbot")
    print("=" * 50)

    name = input("Enter your name: ").strip()

    print(f"\nBot : Welcome {name}! 😊")
    print("Bot : Type 'help' to see available commands.")

    while True:
        user = input(f"\n{name}: ").strip().lower()

        if user in ["hi", "hello", "hey"]:
            print(f"Bot : Hello {name}! Nice to meet you.")

        elif user == "good morning":
            print("Bot : Good Morning! Have a productive day.")

        elif user == "good afternoon":
            print("Bot : Good Afternoon! Hope you're doing well.")

        elif user == "good evening":
            print("Bot : Good Evening! Have a relaxing evening.")

        elif user == "good night":
            print("Bot : Good Night! Sweet dreams.")

        elif user == "how are you":
            print("Bot : I'm doing great. Thanks for asking!")

        elif user == "your name":
            print("Bot : I am CodeAlpha Smart Chatbot.")

        elif user == "who created you":
            print("Bot : I was created by Thirisha using Python.")
        elif user == "who are you":
            print("Bot : I am CodeAlpha Smart Chatbot, created to help you.")

        elif user == "help":
            show_commands()

        elif user == "thanks":
            print("Bot : You're welcome! Happy Coding!")

        elif user == "bye":
            print(f"Bot : Goodbye {name}! Have a wonderful day! 👋")
            break

        else:
            print("Bot : Sorry, I didn't understand that.")
            print("Bot : Please type 'help' to see available commands.")


if __name__ == "__main__":
    chatbot()
