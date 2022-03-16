# ConnectBan

Tento program poslouchá na zvoleném tcp portu a pokud se na něho někdo bude snažit připojit, tak ho přidá do iptables jako DROP pravidlo  

## Instalace

```bash
# Run as root
iptables -N ssh-filter                    # create the ssh-filter chain
iptables -I INPUT -j ssh-filter           # Add chain to the top
iptables-save > /etc/iptables/rules.v4    # save 

make install 
```

## Spuštění

```bash
# Run as root
systemctl start connectban  # Start the service
systemctl enable connectban # Start service on boot
```
