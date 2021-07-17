# Pyramids Hotel
## _Hotel website and managment system_



Pyramids is a cloud-enabled, mobile-ready, Django-powered Web application.


## Features

- Dynamic content fully customizable through admin panel
- User Registeration/Login
- Authorization feature to limit unrestrictive access
- Booking system
- Admin panel



This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

- Django - Web Application Framewoek
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
 .\env\Scripts\activate
```
Install Requirment Packages
```sh
 pip install -r requirement.txt
```
Migrate Database :
```sh
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
 .\env\Scripts\activate
```
Install Requirment Packages
```sh
 pip install -r requirement.txt
```
Migrate Database :
```sh
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
