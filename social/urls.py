from django.urls import path
from social import views

urlpatterns = [
    path('', views.ApiRoot.as_view(),
        name=views.ApiRoot.name),

    path('profile/', views.ProfileList.as_view(),
        name='profile-list'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(),
        name='profile-detail'),

    path('comment/', views.CommentList.as_view(),
        name='comment-list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(),
        name='comment-detail'),

    path('post/', views.PostList.as_view(),
        name='post-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(),
        name='post-detail'),

    path('profile-posts/', views.ProfilePostsList.as_view(), 
        name='profile-posts-list'),
    path('profile-posts/<int:pk>/', views.ProfilePostsDetail.as_view(), 
        name='profile-posts-detail'),

    path('posts-comments/', views.PostCommentsList.as_view(), 
        name='posts-comments-list'),
    path('posts-comments/<int:pk>/', views.PostCommentsDetail.as_view(), 
        name='posts-comments-detail'),

    path('posts/<int:pk>/comments/', views.AllCommentsPostDetail.as_view(), 
        name='all-comments-post-detail'),
    path('posts/<int:postId>/comments/<int:pk>/', views.AllCommentsAllPostsDetail.as_view(), 
        name='all-comments-all-posts-detail'),

    path('user-statistics/<int:pk>', views.UserStatisticsList.as_view(),
        name='user-statistics-list'),

]
