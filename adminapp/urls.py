from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.ShopUserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.ProductCategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/<int:pk>/', adminapp.ProductReadView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]