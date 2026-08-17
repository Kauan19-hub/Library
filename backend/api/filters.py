import django_filters as df
from django.db.models import Q
from .models import Author, Book, Publisher

class BookFilter(df.FilterSet):
    id=df.NumberFilter(field_name='id',lookup_expr='exact')
    title=df.CharFilter(field_name='title',lookup_expr='icontains')
    subtitle=df.CharFilter(field_name='subtitle',lookup_expr='icontains')
    author=df.CharFilter(field_name='author',lookup_expr='icontains')

    class Meta:
        model=Book
        fields=[]

class AuthorFilter(df.FilterSet):
    id=df.NumberFilter(field_name='id',lookup_expr='exact')
    author=df.CharFilter(field_name='author', lookup_expr='icontains')
    s_author=df.CharFilter(field_name='s_author',lookup_expr='icontains')
    birth=df.CharFilter(field_name='birth',lookup_expr='iexact')

    class Meta:
        model=Author
        fields=[]
        
class PublisherFilter(df.FilterSet):
    id=df.NumberFilter(field_name='id',lookup_expr='exact')
    publisher=df.CharFilter(field_name='publisher',lookup_expr='icontains')

    class Meta:
        model=Publisher
        fields=[]
