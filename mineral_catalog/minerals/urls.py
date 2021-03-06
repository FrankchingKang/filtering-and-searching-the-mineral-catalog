from django.urls import path
from . import views

app_name = 'minerals'

urlpatterns = [
    path('create_database',views.minerals_create),
    path('list', views.mineral_list, name="list"),
    path('list/<slug:letter>', views.mineral_alpha_list, name="alpha_list"),
    path('list/group/<str:group>', views.mineral_group_list, name="group_list"),
    path('search', views.search, name="search"),
    path('detail/<int:pk>', views.mineral_detail, name="detail"),
    path('random/detail', views.mineral_random_detail, name="random"),
]
