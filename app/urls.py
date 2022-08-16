from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("telephone/", numberGenerator.as_view(), name="numbergen"),
    path("cpf/", cpfGenerator.as_view(), name="cpfgen"),
    path("cnpj/", cnpjGenerator.as_view(), name="cnpjgen"),
    path("person/", personGenerator.as_view(), name="persongen"),
]
