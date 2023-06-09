from django.urls import path
from .views import PostsList, PostDetail, Test2, PostEdit, PostDelete, PostCreate

urlpatterns = [
    path('', PostsList.as_view(), name=''),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', Test2.as_view()),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/del/', PostDelete.as_view(), name='post_delete'),
    path('add/', PostCreate.as_view(), name ='post_create')

]