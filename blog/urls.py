from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>', views.post, name="post"),
    path('post-create/', views.createpost, name="post-create"),
    path('post-all/', views.allblog, name="allblog"),
    path('post-update/<str:pk>', views.updatepost, name="post-update"),
    path('post-delete/<str:pk>', views.deletepost, name="post-delete"),
    path('profile/<str:pk>', views.userProfile, name="userprofile"),
    path('profile-edit/<str:pk>', views.editUserProfile, name="edituserprofile"),
    path('profile-login', views.loginUserProfile, name="loginuserprofile"),
    path('profile-logout', views.logoutUserProfile, name="logoutuserprofile"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)