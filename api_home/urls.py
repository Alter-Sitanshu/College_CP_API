from django.urls import path
from .views import HomeView,DeleteView,UpdateView,DetailView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auth/', obtain_auth_token, name='token'),
    path('<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('<int:pk>/update', UpdateView.as_view(), name='update'),
    path('<int:pk>', DetailView.as_view(), name='detail'),
]