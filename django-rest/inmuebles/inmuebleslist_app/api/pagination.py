from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class InmueblePagination(PageNumberPagination):
    
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'
    
class InmuebleLOPagination(LimitOffsetPagination):
    
    default_limit = 1