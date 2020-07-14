from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ArticleAPIView, ArticleDetails, UserAPIView, UserProfile


urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:id>', ArticleDetails.as_view()),
    path('users/', UserAPIView.as_view()),
    path('users/<int:id>', UserProfile.as_view()),
    path('auth/', obtain_auth_token)
]