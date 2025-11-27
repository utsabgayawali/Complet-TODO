from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('clone/',views.clone,name='clone'),
    path('home3/',views.home3,name='home3'),
    path('home4/',views.home4,name='home4'),
    path('home5/',views.home4,name='home5'),
   
]
