from django.urls import path
from .views import signup_view, login_view, logout_view
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('post/new/', create_post_view, name='post_create'),
    path('post/<int:pk>/edit/', update_post_view, name='post_update'),
    path('post/<int:pk>/delete/', delete_post_view, name='post_delete'),

]
