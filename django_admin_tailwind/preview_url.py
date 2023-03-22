from django.template import loader


def get_format_html_preview_url(url, url_text):
    template = loader.get_template('django_admin_tailwind/preview_url.html')
    return template.render({
        'url': url,
        'url_text': url_text
    })
