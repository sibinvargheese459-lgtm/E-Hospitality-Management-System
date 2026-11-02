from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.BillListView.as_view(), name='list'),
    path('add/', views.BillCreateView.as_view(), name='add'),
    path('<int:pk>/', views.BillDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BillUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BillDeleteView.as_view(), name='delete'),
]
