from rest_framework import serializers
from .models import Author, Publisher, Book, Image
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    capa_url = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = [
            "id",
            "title", 
            "subtitle", 
            "author", 
            "publisher", 
            "isbn", 
            "description", 
            "language", 
            "year", 
            "pages", 
            "price", 
            "stock", 
            "discount", 
            "available", 
            "dimensions", 
            "width", 
            "cover",
            "cover_url",  
        ]

    def get_cover_url(self, obj):
        request=self.context.get("request")
        if obj.cover and request:
            return request.build_absolute_uri(obj.cover.url)  
        return None
        
User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username=serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),message="Usuário já existe.")]
    )

    password=serializers.CharField(
        write_only=True,required=True,validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model=User
        fields=('id', 'username', 'password')

    def create(self,validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
    
class ImageSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField()

    class Meta:
        model=Image
        fields=['id','image','url','created_at']
        read_only_fields=['id','url','crieated_at']

    def get_url(self,obj):
        request=self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.imagem.url)
        return obj.imagem.url
