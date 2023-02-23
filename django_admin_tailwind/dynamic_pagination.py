import django.contrib.admin.views.main


class DynamicPaginationChangeList(django.contrib.admin.views.main.ChangeList):
    dynamic = True

    def __init__(
        self,
        request,
        model,
        list_display,
        list_display_links,
        list_filter,
        date_hierarchy,
        search_fields,
        list_select_related,
        list_per_page,
        list_max_show_all,
        list_editable,
        model_admin,
        sortable_by
    ):
        page_param = request.GET.get('list_per_page', None)
        if page_param is not None:
            list_per_page = int(page_param)
        super(DynamicPaginationChangeList, self).__init__(
            request,
            model,
            list_display,
            list_display_links,
            list_filter,
            date_hierarchy,
            search_fields,
            list_select_related,
            list_per_page,
            list_max_show_all,
            list_editable,
            model_admin,
            sortable_by
        )

    def get_filters_params(self, params=None):
        lookup_params = super(DynamicPaginationChangeList, self).get_filters_params(params)
        if 'list_per_page' in lookup_params:
            del lookup_params['list_per_page']
        return lookup_params
