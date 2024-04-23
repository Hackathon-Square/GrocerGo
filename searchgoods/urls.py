from django.urls import path
from . import views
from .views import upload_image  # make sure to import your view function

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    #path('', lambda request: redirect('search_results')),
    path('upload-image/', upload_image, name='upload_image')
]


