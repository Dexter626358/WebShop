from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('contacts/', views.contacts, name='get_contacts'),
    path('fake/product', views.generate_fake_products, name='fake_products'),
    path('fake/client', views.generate_fake_clients, name='fake_clients'),
    path('registr/', views.register_client, name='create_client'),
    path('clients/', views.get_all_clients, name='get_all_clients'),
    path('client/<int:client_id>/', views.search_client_by_id, name='get_client_by_id'),
    path('client/delete/<int:client_id>/', views.delete_client, name='delete_client'),

]
