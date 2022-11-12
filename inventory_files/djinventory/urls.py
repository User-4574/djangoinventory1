from django.urls import path, include
from rest_framework import routers
from . import views
import private_storage.urls
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
router = routers.DefaultRouter()
from django.conf import settings
from django.conf.urls.static import static


#The extra URLS are for client testing
#router.register(r'sys_checkin', views.syscheckinsViewSet)

urlpatterns = [
#	path('', views.index, name='index'),
#	path('private-media/', include(private_storage.urls)),
	path('admin/', admin.site.urls, name='administrator'),
	path('admin/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#	path('', include('social_django.urls', namespace='social')),
#	path(
#		'logout/',
#		LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
#		name='logout'
#	),
#	path('manage/', views.manage, name='manage'),
]