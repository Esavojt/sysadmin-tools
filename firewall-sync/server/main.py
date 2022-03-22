import json
import re
import socket

iptables_regex = "DROP +all +-- +(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) +0\.0\.0\.0\/0 *"
exit()