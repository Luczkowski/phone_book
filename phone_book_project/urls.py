from django.contrib import admin
from django.urls import path
from phone_book_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.phone_book, name="phone_book"),
    path('new/', views.new_person, name="new_person"),
    path('edit/<int:id>', views.edit_person, name="edit"),
    path('delete/<int:id>', views.delete_person, name="delete"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('new_phone/<int:id>', views.new_phone, name="new_phone"),
    path('new_email/<int:id>', views.new_email, name="new_email"),
    path('search/', views.SearchResultsView.as_view(), name="search"),
]
