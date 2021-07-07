from django.utils import lorem_ipsum
from django.core import management
from model_bakery import baker
from app.models import TagModel


class Command(management.base.BaseCommand):

    def handle(self, *args, **options):
        management.call_command('loaddata', 'default_users')
        tag_1, _ = TagModel.objects.get_or_create(name="200")
        tag_2, _ = TagModel.objects.get_or_create(name="300")
        baker.make(
            'app.DataModel',
            _quantity=200,
            long_long_long_long_long_char_field=lorem_ipsum.words(100),
            text_field=lorem_ipsum.paragraphs(3),
            number_field=200,
            url_field='http://django.tailwind',
            tag=tag_1,
        )
        baker.make(
            'app.DataModel',
            _quantity=300,
            long_long_long_long_long_char_field=lorem_ipsum.words(100),
            text_field=lorem_ipsum.paragraphs(3),
            number_field=300,
            url_field='http://django.tailwind',
            tag=tag_2
        )
