from django.urls import path
from .import views as v
urlpatterns = [
    path('', v.todoView, name='index'),
    path('addTodo/', v.addTodo, name='addTodo'),
    path('deletetodo/<int:id>', v.deletetodo, name='deletetodo')
]
