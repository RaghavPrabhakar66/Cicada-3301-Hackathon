from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('datasets/', views.datasets , name='datasets'),
    path('create/', views.createDataset, name='create'),
    path('datasets/<int:dataset_id>/', views.explore, name='explore'),
    path('contribute/<int:dataset_id>/', views.contribute, name = 'contribute'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)