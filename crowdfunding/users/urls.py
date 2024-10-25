from django.urls import path
from .views import CustomUserList, CustomUserDetail

urlpatterns = [
    path('users/', CustomUserList.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
]




################ V1 ##############

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('users/', views.CustomUserList.as_view()),
#     path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    
# ]



