from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/activity/', views.ActivityList.as_view()),
    path('api/user/',views.UserAccountList.as_view())
]
