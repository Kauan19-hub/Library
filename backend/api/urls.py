from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorsView, AuthorsDetailView, list_authors,
    PublisherView, EditorasDetailView,
    ImagemViewSet, LivroViewSet, RegisterView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()  # gera barra final nas rotas
router.register(r"imagens", ImagemViewSet, basename="imagens")
router.register(r"livros",  LivroViewSet,  basename="livro")   # <-- esta linha

urlpatterns = [
    path('autores/', AutoresView.as_view(), name='autores-list'),
    path('autor/<int:pk>', AutoresDetailView.as_view(), name='autores-detail'),
    path('authors', listar_autores, name='Listar Autores'),

    path('editoras/', EditorasView.as_view()),
    path('editora/<int:pk>/', EditorasDetailView.as_view()),

    # NÃO repita rotas de livros aqui (remova estas se existirem):
    # path('livros', LivrosView.as_view()),
    # path('livro/<int:pk>', LivrosDetailView.as_view()),

    path('token/',   TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(),     name='token_refresh'),
    path('register/', RegisterView.as_view(),        name='register'),
]

urlpatterns += router.urls
