mkvirtualenv --python python2.7 django-dummy-app
pip install -r requirements.pip 
pip install -r requirements-dev.pip


# Testing

http://localhost:8000/store/beers/ is a view that should return a JSON dict with all the beers available


# To Improve

Move the apps to the same level in the fs as dummy/ (e.g. store/ beers/ dummy/), instead of below (e.g. dummy/store/ dummy/beers/)