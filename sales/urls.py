from django.urls import path
from sales import views
from sales.views import *

urlpatterns = [
    path('saleslist/', views.SalesListView.as_view()),
    path('saleslist/<int:pk>/', views.SalesDetailView.as_view()),
    path("sale_report/", SaleReportView.as_view(),name="sale_report"),
]
