from django.conf import settings
import os
import json
import pkg_resources

if settings.DEBUG:
    with open(os.path.join(settings.BASE_DIR, 'package.json')) as package:
        data = json.load(package)
        VERSION = data['version']
else:
    VERSION = pkg_resources.get_distribution("django-admin-tailwind").version
