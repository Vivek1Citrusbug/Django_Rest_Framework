from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

class MyPaginator(PageNumberPagination):
    # Only display 10 blogs per page
    page_size = 10

class myOrderingFilter(OrderingFilter):
    pass