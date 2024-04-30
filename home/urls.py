from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.create_person, name='create_person'),
    path('', views.person_list, name='person_list'),
    path('<int:person_id>/', views.person_detail, name='person_detail'),
    path('<int:person_id>/update/', views.update_person, name='update_person'),
    path('<int:person_id>/delete/', views.delete_person, name='delete_person'),
]

