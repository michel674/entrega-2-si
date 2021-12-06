from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('create/', views.CreateView, name='create'),
    path('categories/', views.ListCategoryView.as_view(), name='list_categories'),
    path('categories/<int:category_id>', views.DetailCategory, name='list_posts_per_category'),
    path('<int:post_id>/', views.DetailView, name='detail'),
    path('<int:post_id>/comment/',views.create_comment, name = 'comment'),
    path('update/<int:post_id>/', views.UpdateView, name='update'),
    path('delete/<int:post_id>/', views.DeleteView, name='delete'),
]
