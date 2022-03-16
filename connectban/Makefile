CC=clang

compile:
	$(CC) -o connectban main.c

install: compile install-etc

install-etc:
	install -m 755 connectban /usr/bin/
	install -m 644 connectban.service /etc/systemd/system/
