from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/',views.snippet_detail),
    path('users/', views.UserList, name='users'),
    path('users/<int:pk>/', views.UserDetail, name='users_detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
