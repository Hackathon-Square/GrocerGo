from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('results/', views.search_results, name='search_results'),
    #path('', lambda request: redirect('search_results')),
    path('search_upload_image/', views.search_upload_image, name='search_upload_image')
]


