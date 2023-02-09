from django.contrib.admin.filters import AllValuesFieldListFilter, RelatedFieldListFilter


class DropdownRelatedFilter(RelatedFieldListFilter):
    template = 'django_admin_tailwind/dropdown_filter.html'


class DropdownValuesFilter(AllValuesFieldListFilter):
    template = 'django_admin_tailwind/dropdown_filter.html'
