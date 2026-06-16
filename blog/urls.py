from django.urls import path
from . import views
from django.contrib.auth import views as auth

app_name = 'blog'
urlpatterns = [
  #path('', views.post_list, name='post_list'),
  #path('<int:id>/', views.post_detail, name='post_detail'),
  path('', views.book_list, name='book_list'),
  path('book/<int:book_id>/', views.book_detail, name='book_detail'),
  path('', views.user_book_list, name='user_book_list'),
  path('<int:id>/', views.user_book_detail, name='user_book_detail'),
  path('user_book/add_book/', views.add_book, name='add_book'),
  path('Main_Page/', views.index, name='index'),
  path('Profile/', views.edit_profile, name='edit_profile'),
  path('search/', views.search_books, name='search_books'),
  path('serch/', views.search_results, name='results'),
  path('get_error/', views.error, name='err'),
  path('registration/', views.registr, name='registr'),
  path('logout/', auth.LogoutView.as_view(next_page='blog:index', template_name='blog/logout/logout.html'), name='logout'),
  path('login/', views.Login, name='Login'),
]
