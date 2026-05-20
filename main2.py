def print_welcome():
    try:
        # Ask the user for their name (optional)
        name = input("Enter your name (or press Enter to skip): ").strip()

        if name:  # If the user entered a name
            print(f"Welcome, {name}!")
        else:  # If no name entered
            print("Welcome!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    print_welcome()

