from django.urls import path
from guest_book.views import index_view, delete_view, create_view, update_view

urlpatterns = [
    path('', index_view, name="index"),
    path('entry/add/', create_view, name="create"),
    path('enty/<int:pk>/update/', update_view, name="update"),
    path('entry/<int:pk>/delete/', delete_view, name="delete")
]