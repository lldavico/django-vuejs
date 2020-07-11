from django.urls import path
from .views import HomeAPIView, ArticleAPIView, ArticleDetails
# from .views import article_list, article_detail


urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),
    path('', HomeAPIView.as_view())
]

'''
urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:pk>/', article_detail)
]
'''