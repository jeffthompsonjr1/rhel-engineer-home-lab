#!/bin/bash

#==== Posistional Arguments ====

echo "=== Positional Arguments ==="
echo "Script Name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total number of arguments: $#"
echo "All arguments: $@"
echo -e "\n"

# ==== Using Return Codes ====
echo "=== Return Codes ==="
echo "Attempting to list a directory..."
ls "$1" >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Success: Directory '$1' exists."
else
    echo "Error: Directory '$1' not found."
fi
echo


# ==== Demonstrating Arrays ===
echo "=== Arrays ==="
my_array=("mango" "pineapple" "plum")
echo "Full array ${my_array[@]}"
echo "First index: ${my_array[0]}"
echo "Second index: ${my_array[1]}"
echo "Third index: ${my_array[2]}"

# Add an index to the array (if provided)
if [ -n "$3" ]; then
    my_array+=("$3")
    echo "Added '$3' to array. New array: ${my_array[@]}"
fi

# Exit with a custom return code
echo
echo "Exiting with return code 0 (success)."
exit 0


