# Pyramids Hotel
## _Hotel website and Booking system_



Pyramids is a cloud-enabled, mobile-ready, Django-powered Web application.


## Features

- Dynamic content fully customizable through admin panel
- User Registeration/Login
- Authorization feature to limit unrestrictive access
- Booking system
- Admin panel
- Multiple Themes


## Tech

- Django - Web Framewoek
- Pycharm - Python IDE
- HTML/CSS - Creating and Styling Web pages 
- JavaScript - Interactive content and Form validation


# Installation
How to Setup in Windows/MAC/Linux:

Clone this Project :

```sh
git clone https://github.com/AboElmagd01/meta.git
```

Go to Project Directory cd meta :
```sh
 cd meta
```
## Windows Installation:

Create a Virtual Environment :
```sh 
 python -m venv env
```
Activate Virtual Environment 
```sh
 . \env\Scripts\activate
```
Install Requirment Packages
```sh
 pip install -r requirements.txt
```
Migrate Database :
```sh
  py manage.py makemigrations
  py manage.py migrate
```
Create SuperUser :
```sh
 py manage.py createsuperuser
 ```
Finally Run the Projects :
```sh
 py manage.py runserver
```

## Linux Installation:

Create a Virtual Environment :
```sh 
 python3 -m venv env
```
Activate Virtual Environment 
```sh
 source mypython/bin/activate
```
Install Requirment Packages
```sh
 pip install -r requirements.txt
```
Migrate Database :
```sh
  python3 manage.py makemigrations
  python3 manage.py migrate
```
Create SuperUser :
```sh
 python3 manage.py createsuperuser
 ```
Finally Run the Projects :
```sh
 python3 manage.py runserver
```
