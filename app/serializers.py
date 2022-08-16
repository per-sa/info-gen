from rest_framework import serializers


class brazilian_phone_number_serializer(serializers.Serializer):
    ddd = serializers.CharField()
    unformated = serializers.CharField()
    generated_number = serializers.CharField()


class cpf_serializer(serializers.Serializer):
    unformated = serializers.CharField()
    generated_cpf = serializers.CharField()


class cnpj_serializer(serializers.Serializer):
    unformated = serializers.CharField()
    generated_cnpj = serializers.CharField()
