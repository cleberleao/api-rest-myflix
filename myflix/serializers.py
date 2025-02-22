from rest_framework import serializers
from myflix.models import user, stream, lista

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class streamSerializer(serializers.ModelSerializer):
    class Meta:
        model = stream
        fields = '__all__'

class listaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista
        exclude=[]

class listaUserSerializer(serializers.ModelSerializer):
    stream = serializers.ReadOnlyField(source='stream.descricao')

    class Meta:
        model = lista
        fields = ['stream']


class listaStreamSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['user_nome']