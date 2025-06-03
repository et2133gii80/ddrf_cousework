from rest_framework.pagination import PageNumberPagination


class ViewUserHabitPagination(PageNumberPagination):
    page_size = 5