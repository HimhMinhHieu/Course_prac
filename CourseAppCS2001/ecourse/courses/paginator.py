from rest_framework.pagination import PageNumberPagination


class CourseSetPagination(PageNumberPagination):
    page_size = 2