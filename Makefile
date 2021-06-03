start:
	python manage.py runserver localhost:4243 -v 3

mm:
	python manage.py migrate

patch:
	npm version patch
	git push --tags origin master
