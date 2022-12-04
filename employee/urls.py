from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<employee_id>', views.delete, name="delete"),
    path('edit/<employee_id>', views.edit, name="edit")
]