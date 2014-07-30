# Installation

Install system (aptitude) dependencies before pip dependencies for a seamless install.

## Aptitude


- RabbitMQ: follow [Install RabbitMQ on Debian](http://www.rabbitmq.com/install-debian.html)
- mysql-server
- libmysqlclient-dev
- apache2
- libapache2-mod-wsgi
- python-pip

## Pip

This uses virtualenv. To setup virtualenv take the following steps:

- <code>sudo pip install virtualenv</code>
- <code>sudo pip install virtualenvwrapper</code>
- Paste this is your  ~/.bashrc:

```
# Python virtualenv stuff
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export WORKON_HOME=/virtualenvs
source "$(which virtualenvwrapper.sh)"
```

- Create and change the owner of /virtualenvs to you: <code>sudo chown $USER:$USER /virtualenvs/</code>

- Source your new ~/.bashrc: <code>source ~/.bashrc</code>

- Create the virtualenv operon-evo-db: <code>mkvirtualenv operon-evo-db</code>

Either use the deps.cfg in the repository to download all dependencies at once or install individually.

To install all at once run: <code>pip install -r deps.cfg</code>.

## Django App Setup

For the remainder of the install instructions let <code>$APP</code> stand for the directory you
have chosen for the Github repo. i.e. if you cloned this repo to be /env/OperonEvoDB/ then that is
the value for $APP.

### Setup MySQL Database

- Create a database name 'operonevodb' and grant all privileges on that database to a user of your
choosing. (You can change the name of the database if you want just change it in the next step).

- Create the file <code>$APP/config/db.json</code> to contain your database information. It should
have the following format:

```
{
    "name": "operonevodb",
    "user": "<username>",
    "password": "<password>",
    "host": "",
    "port": ""
}
```

The host and port should be left empty if the MySQL database being used is on the same machine. This
exact file is marked in the .gitignore to never commit to git, so you won't expose your database info.

- In $APP, run <code>python manage.py syncdb</code>. If this is successful, you've done everything
correctly and your database should be loaded with the correct tables.

### Setup Apache

- Edit the file <code>$APP/operonevodb.conf</code> by replacing all occurrences of $APP in the file
with the value of $APP i.e. /env/OperonEvoDB.

- Move $APP/operonevodb.conf to /etc/apache2/sites-available/.
<code>mv $APP/operonevodb.conf /etc/apache2/sites-available/</code>

- Edit

- Disable the default site, <code>sudo a2dissite default</code>

- Enable the operonevodb site, <code>sudo a2ensite operonevodb.conf</conf>

# Using the OperonEvoDB models in a terminal python script

Once again, let $APP represent the place in which you cloned this repository.

```
# Adding the Django settings to properly configure the models and project
import os, sys

sys.path.append('$APP')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
```
