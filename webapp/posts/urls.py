from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'posts'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password-reset', views.PasswordsResetView.as_view(), name='password_reset'),
    path('password-reset/done', views.PasswordsResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', views.PasswordsResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', views.PasswordsResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.PostsView.as_view(), name='postsview'),
    path('createpost', views.PostsCreateView.as_view(), name='createpost'),
    path('comment/post<int:pk>', views.CommentCreateView.as_view(), name='comment'),
    path('postupdate/post<int:pk>', views.PostsUpdateView.as_view(), name='postupdate'),
    path('postdelete/post<int:pk>', views.PostsDeleteView.as_view(), name='postdelete'),
    path('postdeletecomments/post<int:pk>', views.PostsDeleteCommentsView.as_view(), name='postdeletecomments'),
]
