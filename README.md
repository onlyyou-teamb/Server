# :high_brightness: OnlyYou : Automatic face replacement in pictures 
## :arrow_forward: For keeping other's portrait rights safe


> &#9989; &#10102; We generate faked faces to replace with other's faces in your pictures  :open_mouth::camera:

> &#9989; &#10103;  We take care of your original pictures and generated pictures  &#128140;

> &#9989; &#10104; 


<!-- blank line -->
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.gpl-license.org)


## Installation

**Requirements**

Python : 3.7.0 or later (3.6 may compatible)

Opencv-Python : 4.0.0 or later

### Clone

- Clone this repo to your local machine using `https://github.com/laji-cau/LAJI-HIGHLIGHTING.git`

### Dockerizing

- Later on

### Setup

To install the current release for Ubuntu server.
```bash
sudo apt update
sudo apt install git python3-venv libsm6 libxext6 libxrender1 ffmpeg

git clone https://github.com/laji-cau/LAJI-HIGHLIGHTING
cd LAJI-HIGHLIGHTING/

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
#### *Try run LAJI-HIGHLIGHTING*
Add your public IP or DNS to allow hosts.
```bash
$ vim django_capstone/settings
```
```python
ALLOWED_HOSTS = [
    'ADD YOUR PUBLIC IP or DNS',
    'localhost',
    '127.0.0.1',
]
```

This service provides with google login.<br/>
So, you have to activate [GOOGLE+ API](https://console.developers.google.com/apis/api/plus.googleapis.com),
and to create [OAuth 2.0 Client](https://console.developers.google.com/apis/credentials) as a 'web application',
and get API Key/Secret
```bash
$ vim Bash_dir/envs.json
```
```python
{
  "GOOGLE_KEY": "YOUR API_KEY",
  "GOOGLE_SECRET": "YOUR API_SECRET"
}
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8080
```

## Features

> :thumbsup: 
>> `something`

> :astonished:

## Usage

- 

## How to contribute

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/laji-cau/LAJI-HIGHLIGHTING`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request 

---

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © OnlyYou-Team
