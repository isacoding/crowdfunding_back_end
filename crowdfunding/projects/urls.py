from django.urls import path
from .views import ProjectList, ProjectDetail, PledgeList

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', PledgeList.as_view(), name='pledge-detail'),
]



############## V1 ###############

# from django.urls import path
# from . import views

# urlpatterns = [
#      path('projects/', views.ProjectList.as_view()),
#      path('projects/<int:pk>/', views.ProjectDetail.as_view()),
#      path('pledges/', views.PledgeList.as_view())  
# ]


