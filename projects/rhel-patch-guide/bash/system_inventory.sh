#!/bin/bash
# Save the file to system_info with current date time.
system_info="./system_info_$(date +%Y%m%d_%H%M%S).txt"

#Collect user input for the system role and save it in  variable
read -r -p "Enter System Role: " system_role

#Generate the report
cat << EOF > "$system_info"

================= SYSTEM INFO =========================

HOSTNAME:       $(hostname)

OS              $(hostnamectl |grep -Ei "Operating")

KERNEL:         $(uname -r)

ARCH:           $(uname -m)

VIRTUALIZATION: $(hostnamectl |grep -Ei "Virtualization")

SYSTEM ROLE:    $system_role

PATCH HISTORY: 
$(dnf history | head -n 10)

ACTIVE SERVICES: 
$(systemctl list-units --type=service --state=active)

EOF


