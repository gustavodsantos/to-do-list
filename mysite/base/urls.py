from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:tarefa_id>/feita/', views.marcar_como_feita, name='marcar_como_feita'),
    path('tarefa/<int:tarefa_id>/pendente/', views.marcar_como_pendente, name='marcar_como_pendente'),
    path('tarefa/<int:tarefa_id>/apagar/', views.apagar_tarefa, name='apagar_tarefa'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
