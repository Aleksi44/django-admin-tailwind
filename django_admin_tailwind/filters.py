from django.contrib.admin.utils import get_model_from_relation, reverse_field_path
from django.contrib.admin.filters import RelatedFieldListFilter, FieldListFilter
from django.utils.translation import gettext_lazy as _


class DropdownChoiceFilter(FieldListFilter):
    template = 'django_admin_tailwind/filters/dropdown_choice_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = field_path
        self.lookup_kwarg_isnull = '%s__isnull' % field_path
        lookup_val = params.get(self.lookup_kwarg, [])
        if lookup_val:
            lookup_val = lookup_val.split(',')
        self.lookup_val = lookup_val
        self.lookup_val_isnull = params.get(self.lookup_kwarg_isnull)
        self.empty_value_display = model_admin.get_empty_value_display()
        parent_model, reverse_path = reverse_field_path(model, field_path)
        # Obey parent ModelAdmin queryset when deciding which options to show
        if model == parent_model:
            queryset = model_admin.get_queryset(request)
        else:
            queryset = parent_model._default_manager.all()
        self.lookup_choices = queryset.distinct().order_by(field.name).values_list(field.name, flat=True)
        super().__init__(field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def choices(self, changelist):
        yield {
            'selected': not self.lookup_val and self.lookup_val_isnull is None,
            'query_string': changelist.get_query_string(remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]),
            'display': _('All'),
        }
        include_none = False
        for val in self.lookup_choices:
            if val is None:
                include_none = True
                continue
            val = str(val)
            if val in self.lookup_val:
                values = [v for v in self.lookup_val if v != val]
            else:
                values = self.lookup_val + [val]
            if values:
                yield {
                    'selected': val in self.lookup_val,
                    'query_string': changelist.get_query_string({self.lookup_kwarg: ','.join(values)},
                                                                [self.lookup_kwarg_isnull]),
                    'display': val,
                }
            else:
                yield {
                    'selected': val in self.lookup_val,
                    'query_string': changelist.get_query_string(remove=[self.lookup_kwarg]),
                    'display': val,
                }
        if include_none:
            yield {
                'selected': bool(self.lookup_val_isnull),
                'query_string': changelist.get_query_string({self.lookup_kwarg_isnull: 'True'}, [self.lookup_kwarg]),
                'display': self.empty_value_display,
            }


class DropdownRelatedFilter(RelatedFieldListFilter):
    template = 'django_admin_tailwind/filters/dropdown_related_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.app_label = model._meta.app_label
        self.model_name = model._meta.model_name
        self.field_path = field_path
        self.request = request


class DropdownRelatedMultipleFilter(FieldListFilter):
    template = 'django_admin_tailwind/filters/dropdown_related_multiple_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        other_model = get_model_from_relation(field)
        self.lookup_kwarg = '%s__%s__in' % (field_path, field.target_field.name)
        self.lookup_kwarg_isnull = '%s__isnull' % field_path
        self.lookup_val_isnull = params.get(self.lookup_kwarg_isnull)
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_val = self.used_parameters.get(self.lookup_kwarg, [])
        self.lookup_choices = self.field_choices(field, request, model_admin)
        if hasattr(field, 'verbose_name'):
            self.lookup_title = field.verbose_name
        else:
            self.lookup_title = other_model._meta.verbose_name
        self.title = self.lookup_title
        self.empty_value_display = model_admin.get_empty_value_display()
        self.app_label = model._meta.app_label
        self.model_name = model._meta.model_name
        self.field_path = field_path
        self.request = request

    @property
    def include_empty_choice(self):
        return self.field.null or (self.field.is_relation and self.field.many_to_many)

    def has_output(self):
        if self.include_empty_choice:
            extra = 1
        else:
            extra = 0
        return len(self.lookup_choices) + extra > 1

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def field_admin_ordering(self, field, request, model_admin):
        related_admin = model_admin.admin_site._registry.get(field.remote_field.model)
        if related_admin is not None:
            return related_admin.get_ordering(request)
        return ()

    def field_choices(self, field, request, model_admin):
        ordering = self.field_admin_ordering(field, request, model_admin)
        return field.get_choices(include_blank=False, ordering=ordering)

    def choices(self, changelist):
        yield {
            'selected': not self.lookup_val and self.lookup_val_isnull is None,
            'query_string': changelist.get_query_string(remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]),
            'display': _('All'),
        }
        include_none = False
        for val, val_display in self.lookup_choices:
            if val is None:
                include_none = True
                continue
            val = str(val)
            if val in self.lookup_val:
                values = [v for v in self.lookup_val if v != val]
            else:
                values = self.lookup_val + [val]
            if values:
                yield {
                    'selected': val in self.lookup_val,
                    'query_string': changelist.get_query_string({self.lookup_kwarg: ','.join(values)},
                                                                [self.lookup_kwarg_isnull]),
                    'display': val_display,
                }
            else:
                yield {
                    'selected': val in self.lookup_val,
                    'query_string': changelist.get_query_string(remove=[self.lookup_kwarg]),
                    'display': val_display,
                }
        if include_none:
            yield {
                'selected': bool(self.lookup_val_isnull),
                'query_string': changelist.get_query_string({self.lookup_kwarg_isnull: 'True'}, [self.lookup_kwarg]),
                'display': self.empty_value_display,
            }
