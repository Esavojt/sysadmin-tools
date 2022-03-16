import re
import os
import subprocess

# Import the regex for capturing ip addresses
import regexp

# Main function looping
def function():

    # Open the ssh log file and read the contents
    # TODO: Change after testing
    with open("./test-auth.log", "r") as f:
        auth_log = f.read()
    
    # Get all ip addresses in auth.log
    to_ban = re.findall(regexp.ssh_match, auth_log)
    del auth_log
    # Remove duplicates
    to_ban = list(dict.fromkeys([x[1] for x in to_ban])) 
    
    # Check already banned IPs
    result = subprocess.check_output(["iptables", "-L", "ssh-filter", "-n"])
    already_banned = re.findall(regexp.iptables_match, result.decode("utf-8"))

    del result
    
    for ip_to_ban in to_ban:
        # If ip is already banned, ignore
        if ip_to_ban in already_banned:
            continue

        # Ban them
        # TODO: ban
        print(ip_to_ban)
    

