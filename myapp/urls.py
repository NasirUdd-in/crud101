from django.urls import path
from . import views
# from . import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.create_view, name='create'),
    path('list-view/', views.list_view, name='list-view'),
    path('<id>', views.detail_view, name='detail-view'),
    path('<id>/update/', views.update_view, name='update-view'),
    path('<id>/delete/', views.delete_view, name = 'delete-view' ),
    path('login/', views.Login, name= 'login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', views.register, name ='register'),
]
