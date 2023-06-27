from django.urls import path

from . import views 

app_name="event"
urlpatterns = [
    path('create/', views.create_competition, name='competition-create'),
    path('retrieve/', views.retrieve_competitions_list, name='competition-read'),
    path('retrieve/<int:id>', views.get_competition, name='competition-details'),
    path('update/<int:id>', views.update_competition, name='competition-update'),
    path('delete/<int:id>', views.delete_competition, name='competition-delete'),
]
