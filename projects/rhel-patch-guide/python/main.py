import socket, platform


# List of menu selections
welcome_menu = ['Collect System Information','Review Patch Readiness','Post Patch Validation','Generate Report','Exit']

def collect_system_info():
    print("\nCollecting System Information...")




#Function that prints the menu list items
def display_menu():
    print('\n PATCHING PROCEDURE MENU\n')
    while True:
        for i in range(len(welcome_menu)):# For loop through the list by length to add a numbered list.
            print(f"{i+1}. {welcome_menu[i]}") #Print index plus one because index starts at 0, 
                                            #welcome_menu index prints the list position associated in the range
        global option_selection #Global variable to be able to access outside of the function
        try:
            option_selection = int(input("\nEnter an option 1 - 5: ")) # Variable to capture user input for menu options
        except ValueError:
            print('\nInvalid input please enter a valid number\n')
            continue

        if option_selection < 5 and option_selection > 0:
            print(f'\n{option_selection}. {welcome_menu[option_selection - 1]}\n')             
            if option_selection == 1:
                collect_system_info()        
        elif option_selection == 5:
            print("\nExiting Program\n")
            break
        else:
            print("\nInvalid selection. Please enter a number between 1 and 5\n")
       
            
        
display_menu()
