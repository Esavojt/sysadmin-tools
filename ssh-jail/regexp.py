ssh_match = "(?:(?:Invalid)|(?:Connection closed by (?:authenticating|invalid))) user (\w+?) (?:from )?(\d+?\.\d+?\.\d+?\.\d+?) port (\d{1,5})(?: \[preauth\])?"
iptables_match = "DROP +all +-- +(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) +0\.0\.0\.0\/0 *"
ip_match = "((?:[0-9]{1,3}\.){3}[0-9]{1,3})"