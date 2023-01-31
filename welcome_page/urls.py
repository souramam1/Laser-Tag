from django.urls import path
from . import views

###### :8000/other
urlpatterns = [
    #path('',views.simple_view),
    path('about/',views.about_view, name='about'),
    path('software/', views.software_view, name='software' ),
    path('contact/',views.contact_view, name = 'contact')
]