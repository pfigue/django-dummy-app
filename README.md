# Prepare the virtualenv

	$ mkvirtualenv --python python2.7 django-dummy-app

	$ cat > $WORKON_HOME/django-dummy-app/bin/postactivate
	#!/bin/bash
	# This hook is run after this virtualenv is activated.

	export PYTHONPATH=<path_to_project>/django-dummy-app/dummy/
	cd <path_to_project>/django-dummy-app/dummy/
	^D

	$ cat > $WORKON_HOME/django-dummy-app/bin/postdeactivate
	#!/bin/bash
	# This hook is run after this virtualenv is deactivated.

	unset PYTHONPATH
	^D

	(django-dummy-app)$ pip install -r requirements.pip 
	(django-dummy-app)$ pip install -r requirements-dev.pip



# Testing

http://localhost:8000/store/beers/ is a view that should return a JSON dict with all the beers available


# To Improve

Move the apps to the same level in the fs as dummy/ (e.g. store/ beers/ dummy/), instead of below (e.g. dummy/store/ dummy/beers/)