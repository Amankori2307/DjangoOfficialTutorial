from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# from snippets.views import SnippetView
# router = DefaultRouter()
# router.register('snippet',SnippetView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    # path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)