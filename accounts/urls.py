from django.urls import path, include
from . import views

app_name = "accounts_api"

urlpatterns = [
    path('user/', views.check_user.as_view(), name='get_user'),                       #Check user api
    path('auth/', include('dj_rest_auth.urls', namespace='djrest_api')),                #dj rest auth login, change password etc

]