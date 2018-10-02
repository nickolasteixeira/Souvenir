#!/usr/bin/env bash
# Install dependencies and run application
git clone https://github.com/nickolasteixeira/Souvenir.git

sudo apt-get install -y python3-pip
sudo apt-get install -y python-pip
sudo pip3 install --upgrade pip

# postgres dependencies
sed -i "s/'USER': 'vagrant'/'USER': '$USER'/" /home/$USER/Souvenir/souvenir/settings.py
sudo apt-get install -y postgresql libpq-dev postgresql-client postgresql-client-common
sudo -u postgres bash -c "psql -c \"CREATE USER $USER WITH PASSWORD 'root';\""
sudo -u postgres bash -c "psql testpython -c \"GRANT ALL ON ALL TABLES IN SCHEMA public to $USER;\""
sudo -u postgres bash -c "createdb testpython"

#3. Install Django application depedencies
PROJECT="/home/$USER/Souvenir"
cd $PROJECT
sudo pip install -r requirements.txt

# Run application
sudo apt-get install nginx
sudo sed -i 's~try_files $uri $uri/ =404;~proxy_pass http://0.0.0.0:8001/;~' /etc/nginx/sites-available/default
sudo sed -i '38i location /static/ {autoindex off;alias /home/ubuntu/Souvenir/staticfiles/;}' /etc/nginx/sites-available/default
sudo service nginx restart

#create super user
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('vagrant', 'admin@myproject.com', '$DJANGO_PASSWORD')" | python3 manage.py shell


#migrate database
python3 manage.py migrate
