from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_view, name='create'),
    path('list-view/', views.list_view, name='list-view'),
    path('<id>', views.detail_view, name='detail-view'),
    path('<id>/update/', views.update_view, name='update-view'),
    path('<id>/delete/', views.delete_view, name = 'delete-view' )
]
