import socket, platform, os, shutil


# List of menu selections
welcome_menu = ['Collect System Information','Review Patch Readiness','Post Patch Validation','Generate Report','Exit']
critical_disk = ['/','/var','/boot']
def collect_system_info():
    print("\nCollecting System Information...")
    print(f"\nHostname: {platform.node()}")
    print(f"OS Family: {platform.system()}")
    print(f"Machine Architecture: {platform.machine()}")
    print(f"Kernel Release: {platform.release()}")
    os_info = platform.freedesktop_os_release()
    print(f"Distribution: {os_info.get('NAME', 'Unknown')}")
    print(f"Distribution Version: {os_info.get('VERSION_ID', 'Unavailable')}")
    print(f"Logical CPUs: {os.cpu_count()}")
    with open('/proc/meminfo', 'r') as file:
        memory_info = file.read()
    memory_lines = memory_info.splitlines()
    for line in memory_lines:
        if line.startswith('MemTotal:'):
            total_memory = line.split()
            print(f"Total memory: {int(total_memory[1])/1024:.2f} MiB")
        elif line.startswith('MemAvailable:'):
            available_memory = line.split()
            print(f"Availiable Memory: {int(available_memory[1])/1024:.2f} MiB")
    not_available_mem = ((int(total_memory[1])-int(available_memory[1]))/int(total_memory[1]))*100
    print(f"% Memory Not Available: {int(not_available_mem):.2f}")
    print("Critical Disk Usage:")
    for disk in critical_disk:
        print(f"{disk}: {shutil.disk_usage(disk)}")
    print()



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
