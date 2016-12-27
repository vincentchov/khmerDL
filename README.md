## Abstract
This is the GitHub repository for KhmerDL, an app that helps you download videos from Khmer sites, with the help of youtube-dl.

## Setup
This project assumes the user will run the app on a Debian-based Linux distro.  If you are using Windows 10, you can enable "Bash on Ubuntu on Windows" to setup an Ubuntu environment.  We also assume you use Python 3.4.

Add ```alias python='python3.4'``` to your .bashrc

In Terminal, install the following dependencies using apt-get:

```
sudo apt-get install python3-pip python-pip git python3-dev python-pip python-dev
```

Clone the repository into a directory of your choosing and cd into it.

```
git clone https://github.com/vincentchov/khmerDL.git
cd khmerDL
```

Create and activate the virtual environment "env", upgrade pip, and install python dependencies.

```
virtualenv -p '/usr/bin/python3.4' env
source env/bin/activate
env/bin/pip install --upgrade pip
pip install -r requirements.txt
```

To run the app, type in ```python khmerDL.py [URL of show page]```.
