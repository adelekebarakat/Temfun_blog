from django.urls import path
from .views import Home, Detail, Createblog, Updateblog, Deleteblog, AddCategory, CategoryView, CategoryViewList, search, CommentSection
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detail/<str:pk>', Detail.as_view(), name='detail'),
    path('createblog', Createblog.as_view(), name='create_blog'),
    path('detail/<str:pk>', Detail.as_view(), name='detail'),
    path('detail/update/<str:pk>', Updateblog.as_view(), name='update_blog'),
    path('detail/<str:pk>/remove', Deleteblog.as_view(), name='delete_blog'),
    path('addcategory', AddCategory.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryViewList, name='category_list'),
    path('search/', search, name='search'),
    path('detail/<int:pk>/comment/', CommentSection.as_view(), name='comment'),
    
]
