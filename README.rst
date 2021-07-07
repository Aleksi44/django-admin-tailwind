*********************
Django Admin Tailwind
*********************

.. image:: https://img.shields.io/pypi/v/django-admin-tailwind
    :target: https://pypi.org/project/django-admin-tailwind/

.. image:: https://img.shields.io/pypi/pyversions/django-admin-tailwind
    :target: https://pypi.org/project/django-admin-tailwind/


`Django Admin <https://docs.djangoproject.com/fr/3.2/ref/contrib/admin/>`_ + `Tailwind <https://tailwindcss.com/>`_ = 🚀

django-admin-tailwind is a theme for Django Admin developed with :

- Tailwind class
- `Tailwind forms <https://github.com/tailwindlabs/tailwindcss-forms>`_
- Tailwind dark mode

**WARNING** : Some Django form fields are not yet developed.

.. image:: https://static.snoweb.fr/images/django-admin-tailwind.original.jpg

Setup
#####

Install with pip :

``pip install django-admin-tailwind``

Add django-admin-tailwind to django apps installed :
::

    INSTALLED_APPS = [
        ...
        'django_admin_tailwind',
        ...
        'django.contrib.admin',
    ]


Dev
###

::

    python manage.py migrate
    python manage.py init

Log in with django:tailwind
