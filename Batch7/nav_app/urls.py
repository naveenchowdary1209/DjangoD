from django.urls import path
from nav_app import views
urlpatterns=[
 path('',views.nav),
 path('fig/',views.ch),
 path('home/',views.homepage),
 path('login/',views.lg),
 path('rg/',views.reg)
]