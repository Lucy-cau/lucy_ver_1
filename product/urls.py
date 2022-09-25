from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    # splash 페이지
    path('', views.splash, name='splash'),
    # 홈페이지
    path('home/', views.home, name='home'),
    
    path('bidformcreate/<int:product_id>', views.bidformcreate, name='bidformcreate'),
    path('purchase/<int:product_id>', views.purchase, name='purchase'),

    path('productformcreate/', views.productformcreate, name='productformcreate'),
    path('detail/<int:product_id>', views.detail, name='detail'),  
    
    # 댓글 생성 post
    path('create_comment/<int:product_id>', views.create_comment, name='create_comment'),  
    # 입찰 생성 post
    path('create_bid/<int:product_id>', views.create_bid, name='create_bid'),
    # 바로구매 post
    path('create_purchase/<int:product_id>', views.create_purchase, name='create_purchase'),

]
