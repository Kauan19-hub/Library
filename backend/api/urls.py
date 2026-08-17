from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (AuthorsView, AuthorsDetailView, list_authors, PublishersView, PublisherDetailView, ImageViewSet, BookViewSet, RegisterView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router=DefaultRouter()
router.register(r"images",ImageViewSet,basename="images")
router.register(r"books",  BookViewSet,basename="book")

urlpatterns = [
    path('authors/', AuthorsView.as_view(),name='authors-list'),
    path('author/<int:pk>',AuthorsDetailView.as_view(),name='authors-detail'),
    path('authors',list_authors,name='List Authors'),

    path('publishers/',PublishersView.as_view()),
    path('publisher/<int:pk>/',PublisherDetailView.as_view()),

    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/',RegisterView.as_view(),name='register'),
]

urlpatterns += router.urls
