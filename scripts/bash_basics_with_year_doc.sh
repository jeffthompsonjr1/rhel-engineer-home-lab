#!/bin/bash

REPORT_FILE=~/system_report.txt
# This is how we create the year doc with the cat <<EOF > This is going to print everything from the EOF to the EOF
cat <<EOF > $REPORT_FILE

==== System Status ====
Uptime: $(uptime -p)
Load Average: $(awk '{print $1, $2, $3}' /proc/loadavg)

==== User Status ====
$(who)

==== Disk Status ====
$(lsblk -fs)

==== Memory Status ====
$(free -m)

==== Most CPU intensive processes ===
$(ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -5)

EOF

echo "System report saved to $REPORT_FILE"
