from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView
from django.conf.urls.static import static
from django.conf import settings
from members.urls import urlpatterns as members_urls


urlpatterns=[
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_view"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView , name="category"),
    path('category-list/', CategoryListView , name="category-list"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)