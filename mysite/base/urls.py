from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),
    path('apagar/<int:tarefa_id>', views.apagar, name='apagar'),
]
