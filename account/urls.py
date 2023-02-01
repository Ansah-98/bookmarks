from django.urls import path
from .views import userlogin
from django.contrib.auth import views as auth_views
from .views import dashboard
urlpatterns = [ #path('login', userlogin , name= 'login')
        path('login', auth_views.LoginView.as_view(),name = 'login'),
        path('logout', auth_views.LogoutView.as_view(),name = 'logout'),
        path('dashboard', dashboard, name = 'dashboard'),
        path('password_change' , auth_views.PasswordChangeView.as_view(), name = 'password_change'),
        path('password_done', auth_views.PasswordChangeDoneView.as_view(), name = 'password_done'),
        path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
        path('password_reset_done' , auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset_uidb64', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
        path('reset_done' ,auth_views.PasswordResetCompleteView.as_view() ,name  = 'password_reset_complete')
]
