from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('insert', views.insertData, name='insertData'),
    path('update/<str:id>', views.updateData, name='updateData'),
    path('delete/<str:id>/', views.deleteData, name='deleteData'),
]