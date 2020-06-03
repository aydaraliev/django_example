from django.urls import path

from . import views

app_name = 'statistics101'

urlpatterns = [
    path('stats', views.OrdersList.as_view(), name='OrdersList'),
    #path('stats/<int:pk>', views.MovieDetail.as_view(), name = 'MovieDetail')
    path('order_stats/<str:report_type>', views.orders_to_html),
    path("order_stats/download/<str:report_type>", views.orders_to_csv)
]