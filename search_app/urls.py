from django.urls import path
from . import views
app_name='search_app'

urlpatterns = [
    path('search-result',views.SearchResult,name="search_result"),
]