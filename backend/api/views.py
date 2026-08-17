from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .models import Author, Publisher, Book, Image
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer, RegisterSerializer, ImageSerializer
from .filters import AuthorFilter, PublisherFilter, BookFilter

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['GET', 'POST'])
def list_authors(request):
    if request.method=='GET':
        queryset=Author.objects.all()
        serializers=AuthorSerializer(queryset,many=True)
        return Response(serializers.data)
    
    elif request.method=='POST':
        serializers=AuthorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorsView(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend, SearchFilter,OrderingFilter]
    ilterset_fields=['id']               
    search_fields=['author','s_author','birth']
    ordering_fields=['id','author']
    ordering=['author']
    filterset_class=AuthorFilter         
    
class AuthorsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[IsAuthenticated]

class PublishersView(ListCreateAPIView):
    queryset=Publisher.objects.all()
    serializer_class=PublisherSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=['id','publisher']
    search_fields=['publisher']
    ordering_fields=['id','publisher']
    ordering=['publisher']

class PublisherDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Publisher.objects.all()
    serializer_class=PublisherSerializer
    permission_classes=[IsAuthenticated]

class BookView(ListCreateAPIView):
    queryset=Book.objects.all().select_related('author')
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['id','title']
    search_fields=['title','subtitle','author']
    ordering_fields=['id','title']
    ordering=['title']

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookViewSet(ModelViewSet):
    queryset=Book.objects.all().select_related('author')
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['title','author__name','auhtor__last_name']
    ordering_fields=['id','title']
    ordering=['title']

class RegisterView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer

    def post(self,request,*args,**kwargs):
        ser=self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user=ser.save()
        refresh=RefreshToken.for_user(user)
        return Response({
            'user': {'id': user.id, 'username': user.username},
            'tokens': {'refresh': str(refresh), 'access': str(refresh.access_token)}
        }, status=status.HTTP_201_CREATED)
            
class ImageViewSet(ModelViewSet):
    queryset=Image.objects.all().order_by("-created_at")
    serializer_class=ImageSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset=Book.objects.select_related("author").order_by("-id")
    serializer_class=BookSerializer
    parser_classes=[MultiPartParser,FormParser]
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields=["title","author__name","author__last_name"]
    ordering_fields=["id","title"]
    ordering=["title"]

    @action(detail=True,methods=["post"],parser_classes=[MultiPartParser, FormParser])
    def cover(self, request,pk=None):
        book=self.get_object()
        file=request.FILES.get("cover")
        if not file:
            return Response(
                {"detail": "Arquivo 'cover' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        book.capa=file
        book.save(update_fields=["cover"])
        return Response(self.get_serializer(book).data,status=status.HTTP_200_OK)
