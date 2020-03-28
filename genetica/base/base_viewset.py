# -*- coding: utf-8 -*-


class BaseViewset(object):

    def get_paginated_data(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data).data

        data = self.serializer_class(instance=queryset, many=True).data

        return data
