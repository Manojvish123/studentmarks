from django.urls import path
from django.contrib import admin
from startapp.views import home,loginpage,logoutpage,marks
urlpatterns = [ 
    path(' ',home),
    path('login/',loginpage),
    path('logout/',logoutpage),
    path('admin/', admin.site.urls),
    path('marks/',marks),

]