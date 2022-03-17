import re
import os
import subprocess

# Import the regex for capturing ip addresses
import regexp
import logger

# Main function looping
def function(debug):

    # Open the ssh log file and read the contents
    with open("/var/log/auth.log", "r") as f:
        auth_log = f.read()
        if debug: logger.debug("Read auth file")
    
    # Get all ip addresses in auth.log
    to_ban = re.findall(regexp.ssh_match, auth_log)
    del auth_log
    # Remove duplicates
    to_ban = list(dict.fromkeys([x[1] for x in to_ban])) 
    if debug: logger.debug(f"IPs to ban {to_ban}")
    
    # Check already banned IPs
    result = subprocess.check_output(["iptables", "-L", "ssh-filter", "-n"])
    already_banned = re.findall(regexp.iptables_match, result.decode("utf-8"))

    del result
    
    for ip_to_ban in to_ban:
        # If ip is already banned, ignore
        if ip_to_ban in already_banned:
            if debug: logger.debug(f"IP '{ip_to_ban}' is already banned, ignoring")
            continue

        # Validate that it really is an IP address
        if re.fullmatch(regexp.ip_match, ip_to_ban) is not None:
            # Ban them
            logger.info(f"Now banning '{ip_to_ban}'")
            os.system(f"iptables -I ssh-filter 1 -s {ip_to_ban} -j DROP")
        else:
            logger.warning(f"IP address '{ip_to_ban}' doesn't match IP regex")
    

