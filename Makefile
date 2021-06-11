start:
	python manage.py runserver localhost:4243 -v 3

mm:
	python manage.py migrate

patch:
	npm version patch
	git push --tags origin master

deploy:
	rm -rf dist/*
	yarn build
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
