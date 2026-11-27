import socket, platform, os, shutil, subprocess


# List of menu selections
welcome_menu = ['Collect System Information','Review Patch Readiness','Post Patch Validation','Generate Report','Exit']
critical_disk = ['/','/var','/boot']
line_break = '='*50
def collect_system_info():
    print("\nCollecting System Information...")
    print("\nOS Information")
    print(line_break)
    print(f"\nHostname: {platform.node()}")
    print(f"OS Family: {platform.system()}")
    print(f"Machine Architecture: {platform.machine()}")
    print(f"Kernel Release: {platform.release()}")
    # os_info = platform.freedesktop_os_release()
    # print(f"Distribution: {os_info.get('NAME', 'Unknown')}")
    # print(f"Distribution Version: {os_info.get('VERSION_ID', 'Unavailable')}\n")
    with open('/etc/os-release', 'r') as file:
     Osinfo=file.readlines()
    for info in Osinfo:
        if info.startswith('NAME'):
            distro_name = info.split('=')
        elif info.startswith('VERSION_ID'):
            distro_version = info.split('=')
    clean_name = distro_name[1].strip().strip('"')
    clean_version = distro_version[1].strip().strip('"')
    print(f"Distribution: {clean_name}")
    print(f"Distribution Version: {clean_version}")
    print("CPU & Memory")
    print(line_break)
    print(f"\nLogical CPUs: {os.cpu_count()}")

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
    print(f"% Memory Not Available: {(not_available_mem):.2f}")
    print("\nCritical Disk Usage:")
    for disk in critical_disk:
        disk_info = shutil.disk_usage(disk)
        print(f"Disk Info Usage for {disk}")
        print(f"Total: {(disk_info.total)/(1024**3):.2f} GiB")
        print(f"Used: {(disk_info.used)/(1024**3):.2f} GiB")
        print(f"Free: {(disk_info.free)/(1024**3):.2f} GiB")
        print(f"Disk Utilization = {((disk_info.used/disk_info.total)*100):.2f}%")
        fs_path_info = os.stat(disk)
        print(f"Path:{disk} Device ID: {fs_path_info.st_dev}\n")
    print("Network Config")
    print(line_break)
    print(f"\nHostname: {socket.gethostname()}")
    print(f"FQDN:  {socket.getfqdn()}")
    network_interfaces = (os.listdir('/sys/class/net'))
    print("Network Interfaces:")
    for interface in network_interfaces:
        with open(f"/sys/class/net/{interface}/operstate", 'r') as file:
            interface_path = file.read().strip()
        with open(f"/sys/class/net/{interface}/address", 'r') as file:
            ip_address = file.read().strip()
        print(f"Interface ID:{interface} State: {interface_path} MAC Address:{ip_address} ")
    print("DNS Nameservers:")
    with open('/etc/resolv.conf', 'r') as file:
     contents = file.readlines()
     for content in contents:
        if content.strip().startswith('nameserver'):
            print(content.strip())
    print("")
    print("Default Gateway:")
    with open('/proc/net/route', 'r') as file:
     contents = file.readlines()
     for content in contents:
        content = content.split()
        if content[1] == '00000000':
            interface = content[0]
            gateway = content[2]
            first_oct = int(gateway[6:8], 16)
            second_oct = int(gateway[4:6], 16)
            third_oct = int(gateway[2:4], 16)
            fourth_oct = int(gateway[0:2], 16)
            gateway = f"{first_oct}.{second_oct}.{third_oct}.{fourth_oct}"
            print(f"Interface: {interface}")
            print(f"Gateway: {gateway}")

    result = subprocess.run(
        ["ip", "-o", "-4", "addr", "show"],
        capture_output=True,
        text=True
    )
    print("\nIPv4 Addresses: ")
    ipv4=result.stdout.splitlines()
    for line in ipv4:
        address=line.split()
        print(f"{address[0]} {address[1]}: \t{address[3]}")
    print("")

    
def review_patch_readiness():
    print("Reviewing Patch Readiness...")
    print(line_break)
    print("Checking for available package updates...")
    result = subprocess.run (
        ["dnf", "-q", "check-update"],
        capture_output=True,
        text=True
    )
    if result.returncode == 100:
        print(f'Status: Updates Available')
        print(f'DNF Exit Code: {result.returncode}\n')
        number=0
        packages=result.stdout.splitlines()
        for package in packages:
            update=package.split()
            # print(f"{number}. {update}")
            if 'Obsoleting' in update:
                            break
            elif len(update) == 3:
                number+=1
                print(f"\n{number}. \nPackage:{update[0]}")
                print(f"Version: {update[1]}")
                print(f"Repository: {update[2]}")

        print(f"\n{line_break}")
        print(f'Total Available Package Updates: {number}')
        print(f"{line_break}\n")
    elif result.returncode == 0:      
        print(f'Status: Updates Not Available')
        print(f'DNF Exit Code: {result.returncode}\n')
    else:
        print(f'Status: An Error Occured')
        print(f'DNF Exit Code: {result.returncode}\n')




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
            elif option_selection == 2:
                review_patch_readiness()        
        elif option_selection == 5:
            print("\nExiting Program\n")
            break
        else:
            print("\nInvalid selection. Please enter a number between 1 and 5\n")
       
            
        
display_menu()
