# Installation

## Aptitude

- mysql-server
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

- Change the owner of /virtualenvs to you: <code>sudo chown $USER:$USER /virtualenvs/</code>

- Source your new ~/.bashrc: <code>source ~/.bashrc</code>

- Create the virtualenv operon-evo-db: <code>mkvirtualenv operon-evo-db</code>

Either use the deps.cfg in the repository to download all dependencies at once or install individually.

To install all at once run: <code>pip install -r deps.cfg</code>.


 

