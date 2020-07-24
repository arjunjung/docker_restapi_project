from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.HomeTemplateView.as_view(), name='home' ),
    path('toys/',views.toy_list, name='toy_list'),
    path('toys/<int:pk>',views.toy_funs, name="toy_funs"),
]
