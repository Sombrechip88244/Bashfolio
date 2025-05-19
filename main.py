import time

def help():
    print("Available commands:")
    print("1. help - Show this help message")
    print("2. exit - Exit the program")
    print("3. time - Show the current time")
    print("4. date - Show the current date")
    print("5. uptime - Show system uptime")
    print("6. whoami - Show current user")
    print("7. about - Show information about me")
    print("8. projects - Show my projects")
    print("9. achievements - Show my achievements")

def exit_program():
    print("Exiting...")
    time.sleep(1)
    print("Goodbye!")
    raise SystemExit

def show_time():
    print("Current time: ", time.strftime("%H:%M:%S"))
    input("Press Enter to continue...")

def show_date():
    print("Current date: ", time.strftime("%Y-%m-%d"))
    input("Press Enter to continue...")

def uptime():
    # This is a placeholder; real uptime would require platform-specific code
    print("System uptime: ", time.strftime("%H:%M:%S"))
    input("Press Enter to continue...")

def whoami(username):
    print("Current user: ", username)
    input("Press Enter to continue...")

def about():
    print("About me: I am a software developer who just likes coding random projects I'm currently still learning to code (-_-).")
    input("Press Enter to continue...")

def projects():
    print("My projects: I have worked on many projects although this is my first main one")
    input("Press Enter to continue...")

def achievements():
    print("Putting Hyprland on old linux laptops")
    input("Press Enter to continue...")

def main():
    print("""
  /$$$$$$                          /$$                                     /$$       /$$          
 /$$__  $$                        | $$                                    | $$      |__/          
| $$  \__/  /$$$$$$  /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$  /$$  /$$$$$$ 
|  $$$$$$  /$$__  $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/| $$__  $$| $$ /$$__  $$
 \____  $$| $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$  \__/| $$$$$$$$| $$      | $$  \ $$| $$| $$  \ $$
 /$$  \ $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$      | $$_____/| $$      | $$  | $$| $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$  | $$| $$| $$$$$$$/
 \______/  \______/ |__/ |__/ |__/|_______/ |__/       \_______/ \_______/|__/  |__/|__/| $$____/ 
                                                                                        | $$      
                                                                                        | $$      
                                                                                        |__/      
    """)

    print(f"Welcome to my bashfolio")

    print("Please Login")
    username = input("Username: ")
    password = input("Password: ")

    print(" ")
    print("Use Help command to see all available commands")

    while True:
        command = input(">> ").strip().lower()
        if command == "help":
            help()
        elif command == "exit":
            exit_program()
        elif command == "time":
            show_time()
        elif command == "date":
            show_date()
        elif command == "uptime":
            uptime()
        elif command == "whoami":
            whoami(username)
        elif command == "about":
            about()
        elif command == "projects":
            projects()
        elif command == "achievements":
            achievements()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
