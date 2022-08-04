from django.urls import path,include,re_path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('',views.PostListView.as_view(),name ='blog_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('/<int:pk>/',views.PostDetailView.as_view(),name ='blog_detail'),
    path('postblog_create/',views.CreatePostView.as_view(),name ='blog_create'),
    path('/update/<int:pk>/',views.PostUpdateView.as_view(),name ='blog_update'),
    path('/delete/<int:pk>/',views.PostDeleteView.as_view(),name ='blog_delete'),
    path('/drafts/',views.DraftListView.as_view(),name ='blog_draft'),
    path('/<int:pk>/comment',views.add_comment_to_post,name ='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.comment_approve,name ='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name ='comment_remove'),
    path('/publish/<int:pk>/',views.post_publish,name ='post_publish'),
]
