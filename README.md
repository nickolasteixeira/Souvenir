# Souvenir
Building the trip you want, based on the recommendations of those you trust.

## Description
Souvenir aims to solve the problem of consolidating all of your friends travel recommendations into on application. Wouldn’t it be better if you could build the base of your next trip around the people you trust recommendations?

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __web server:__ nginx/1.4.6
* __application server:__ Django 2.0.9
* __web server gateway:__ gunicorn (version 19.9.0)
* __database:__ psql (PostgreSQL) 9.3.24
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  * __bash:__ ShellCheck 0.3.3

## Set Up

To set up the application, clone the repository to your server

```bash
git clone https://github.com/nickolasteixeira/Souvenir.git
```

Once cloned, move the install_script.sh to the root of your home file path

```bash
mv Souvenir/install_script.sh .
```

Now you can execute the install_script.sh

```bash
./install_script.sh
```

Move souvenir.conf file to /etc/init/ folder for upstart file, then start your souvenir.conf file
```bash
sudo mv Souvenir/souvenir.conf /etc/init/
```
```bash
sudo service souvenir start
```

Now check to see if you application is running on your server
```bash
sudo service souvenir status
```

It should response with a PID number, something like this:
```bash
souvenir start/running, process 21791
```

Check your server IP address to see if the application is running and voila! You have the Souvenir application running on your server. 

## Testing
TBD

## Authors
* Nickolas Teixeira, [nickolasteixeira](https://github.com/nickolasteixeira) | [@NTTL_    LTTN](https://twitter.com/NTTL_LTTN)
* Greg Dame, [gjdame](https://github.com/gjdame) | [@gjdame](https://twitter.com/gjdame?lang=en)
* Dan Kazemian, [Dkazem91](https://github.com/Dkazem91) | [@Dan_Kazam ](https://twitter.com/Dan_Kazam?lang=en)
