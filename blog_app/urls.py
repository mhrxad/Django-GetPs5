from django.urls import path
from blog_app import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    # path('search', views.search_article.as_view(), name='serach_article'),
    path('<article_id>/<article_title>', views.article_detaild, name='article_detaild'),
    # path('<category_name>', views.article_categories_page, name='article_categories_page'),
]
