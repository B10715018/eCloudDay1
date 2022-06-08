# How to fix Nginx Gateway timeout problem

- If you are using ELB, there is setting on the AWS console to increase the idle timeout

- If there is no ELB, means that you should set the timeout from your web server, in this case is Nginx

- First, SSH into your instance

- Then, go to the configuration file of your Nginx, execute:
```
cd /etc/nginx
```

- Edit our Nginx configuration file by:
```
sudo vi nginx.conf
```

- In  the HTTP section, add the following code, to increase timeout:
```
http {
     fastcgi_read_timeout 300;
     proxy_read_timeout 300;
}
```

- Don't forget to reload your Nginx service:
```
sudo service nginx reload
```

- Your Web server is good to go !!