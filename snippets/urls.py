from django.urls import path, include
from . import views

urlpatterns = [
    path(r"snippet/", views.SnippetList.as_view()),
    path(r"snippet/<int:pk>/", views.SnippetDetail.as_view()),
    path(r"users/", views.UserListView.as_view()),
    path(r"users/<int:pk>/", views.UserRetrieveView.as_view()),
    path(r"api-auth/",include('rest_framework.urls'))
]

