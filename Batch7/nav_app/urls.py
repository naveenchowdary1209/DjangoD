from django.urls import path
from nav_app import views
urlpatterns=[
 path('',views.home,name='home'),
 path('fig/',views.ch),
 path('login/',views.lg),
 path('lg/',views.reg,name="login"),
 path('bt/',views.bthm),
 path('about/',views.about,name='about'),
 path('contact/',views.contact,name='contact'),
 path('rf/',views.rf,name='registration'),
 path('rega/',views.rega,name='rega'),
 
]