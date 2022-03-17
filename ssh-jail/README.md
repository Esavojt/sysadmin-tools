# SSH-Jail

Program který zablokuje špatné pokusy o heslo, pročítá záznamy služby ssh v souboru /var/log/auth.log. Jakmile detekuje pokusy o připojení na server, přidá IP adresu jako DROP pravidlo do iptables

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
systemctl start ssh-jail  # Start the service
systemctl enable ssh-jail # Start service on boot
```
