#!/bin/bash

# insert/update hosts entry
host_name=$1
# find existing instances in the host file and save the line numbers
matches_in_hosts="$(grep -n $host_name /tmp/hosts | cut -f1 -d:)"
host_entry="${host_name}"

if [ ! -z "$matches_in_hosts" ]
then
    echo "Updating existing hosts entry."
    # iterate over the line numbers on which matches were found
    while read -r line_number; do
        # replace the text of each line with the desired host entry
        sudo sed -i '' "${line_number}s/.*/${host_entry} /" /tmp/hosts
    done <<< "$matches_in_hosts"
else
    echo "Adding new hosts entry."
    echo "$host_entry" | sudo tee -a /tmp/hosts > /dev/null
fi
cat /tmp/hosts
