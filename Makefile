start:
	python manage.py runserver localhost:4243 -v 3

mm:
	python manage.py migrate

patch:
	npm version patch
	git push --tags origin master
	rm -rf dist/*
	rm -rf build/*
	yarn build
	cp -R build/django_admin_tailwind/ django_admin_tailwind/static/
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
