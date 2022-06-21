from django.urls import path
from .views import *
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginviews, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    ########################################
    path('', prblem, name='main'),
    path('detail/<int:pk>/', Detail_Views.as_view(), name='detail'),
    path(r'^download/?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
