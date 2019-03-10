from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addSkill, name="addSkill"),
    path('getAllSkills', views.getAllSkills),
    path('deleteSkill/<int:id>', views.deleteSkill)
]
