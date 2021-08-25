from django.urls import path, re_path
from .views import hello, error_unknown, error_test


urlpatterns = [
    re_path(r'hello/$', hello),
    re_path(r'error/unknown/$', error_unknown),
    re_path(r'error/test/$', error_test),
]
