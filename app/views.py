from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response
from .serializers import *

import sys

import random

sys.path.append("app/utils")

from ddd import ddd_dict
from validatecpf import validateGenCpf
from validatecnpj import generate_cnpj

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. Test Response.")


class numberGenerator(views.APIView):
    def get(self, request):

        ddd_rand = random.choice(list(ddd_dict.items()))

        entry = (99, 98)
        random_entry = random.choice(entry)

        number_first = random.sample(range(0, 10), 3)
        number_second = random.sample(range(0, 10), 4)

        format_first = "".join(str(x) for x in number_first)
        format_second = "".join(str(x) for x in number_second)

        unformated_num = f"{ddd_rand[0]}{random_entry}{format_first}{format_second}"
        formated_num = f"({ddd_rand[0]}) {random_entry}{format_first}-{format_second}"

        number_data = [
            {
                "ddd": f"{ddd_rand[0]} - {ddd_rand[1]}",
                "unformated": unformated_num,
                "generated_number": formated_num,
            }
        ]
        serialized = brazilian_phone_number_serializer(number_data, many=True).data
        return Response(serialized)


class cpfGenerator(views.APIView):
    def get(self, request):
        func = validateGenCpf()
        number_data = [{"unformated": func[0], "generated_cpf": func[1]}]
        serialized = cpf_serializer(number_data, many=True).data
        return Response(serialized)


class cnpjGenerator(views.APIView):
    def get(self, request):
        func = generate_cnpj()

        number_data = [{"unformated": func[0], "generated_cnpj": func[1]}]
        serialized = cnpj_serializer(number_data, many=True).data
        return Response(serialized)
