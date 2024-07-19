#task1 
#Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

def get_name(prompt):
    
    while True:
        name = input(prompt).strip()
        if len(name) >= 2:
            return name
        else:
            print("Error: The name must be at least 2 characters long. Please try again.")

def main():
   
    first_name = get_name("Enter your first name: ")
    last_name = get_name("Enter your last name: ")
    
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")

if __name__ == "__main__":
    main()
