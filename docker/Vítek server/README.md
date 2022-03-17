# Docker container pro vítkův web server

Integrovaný web server s apache2 a openssh serverem

```bash
docker run \
-v /docker/files/vitek/authorized_keys:/root/.ssh/authorized_keys \
-it -p 5022:22 -p 5080:80 \
-v /docker/files/vitek/www/html:/var/www/localhost/htdocs \ 
-d --name "Vitek_server" vitserver
```

## Služby poslouchají na

- SSH - 5022
- HTTP - 5080
  
## Nutné pravomoce pro soubor authorized_keys

`-rw------- 1 root root 398 Mar 17 19:38 /docker/files/vitek/authorized_keys`
