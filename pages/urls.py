
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),  # الصفحة الرئيسية
    path('add_tag/', views.add_tag, name='add_tag'),  # صفحة إضافة العلامات
]
