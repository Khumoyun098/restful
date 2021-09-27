from rest_framework import pagination
from rest_framework.response import Response
from django.conf import settings


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'size'
    page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE", 15)

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'current': self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })