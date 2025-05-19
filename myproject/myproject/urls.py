from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
path('', views.index, name='home'),
	path('newnewnew', views.new, name='page2')
]
