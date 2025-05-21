from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('delete-appointment/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('edit-appointment/<int:pk>/', views.edit_appointment, name='edit_appointment'),  # Thêm dòng này\
    path('barbers/', views.barbers, name='barbers'),
]