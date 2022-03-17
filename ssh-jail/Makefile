install:
	mkdir -p /etc/ssh-jail
	cp -R . /etc/ssh-jail
	chmod -R 644 /etc/ssh-jail
	chmod 777 /etc/ssh-jail /etc/ssh-jail/main.py /etc/ssh-jail/config.py
	install -m 644 ssh-jail.service /etc/systemd/system/
