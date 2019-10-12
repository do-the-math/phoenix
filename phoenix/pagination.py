from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework.pagination import PageNumberPagination


class RuckitPaginator(Paginator):
    @cached_property
    def count(self):
        if hasattr(self.object_list, '_count'):
            return self.object_list._count
        return super().count


class RuckitPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    django_paginator_class = RuckitPaginator


class RuckitLargePagination(RuckitPagination):
    page_size = 500
    max_page_size = 5000
