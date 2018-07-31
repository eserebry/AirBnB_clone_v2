#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
location="location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n"sudo chown -R ubntu:ubuntu /data/
sudo sed -i "29i $location" /etc/nginx/sites-available/default
sudo service nginx restart
