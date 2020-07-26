from django.urls import path,include
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('about/',views.about, name='blog-about'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),

]