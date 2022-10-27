from distutils.command.upload import upload
from django.db import models

class Locker(models.Model):
    # SET 에 함수로 
    # product_id = models.ForeignKey(Product, on_delete=models.SET())
    # product 가 아니라 bid 로 연결시켜야할 것 같다.
    location = models.CharField(max_length=30, default='중앙대 310관 1층')
    locker_pw = models.CharField(max_length=10, default='1234')
    locker_status = models.IntegerField(default=0)

    def __str__(self):
      return self.location

class Product(models.Model):
    CATEGORY_CHOICES = (
      ('IT', 'IT/전자기기'),
      ('BOOK', 'book'),
      ('DRESS', '의류'),
      ('GIFTCARD', 'giftcard'),
      ('doll', '인형'),
    )

    title    = models.CharField(max_length=50, verbose_name="상품 이름")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="카테고리")
    image    = models.ImageField(null=True, blank=True, upload_to='product_photo', verbose_name='상품 이미지')
    start_price = models.IntegerField(null=False, blank=False, verbose_name='시작가')
    buyout_price = models.IntegerField(null=False, blank=False, verbose_name='즉시구매가')
    created_at = models.DateTimeField(auto_now_add=True)
    register_time = models.DateTimeField(auto_now_add=True)
    # 0: 상품등록 / 1: 거래성사 
    product_status = models.IntegerField(default=0)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, null=True)

    def __str__(self):
      return self.title

    class Meta:
      ordering = ['-created_at']


class Bid(models.Model):
    # user_id = models.ForeignKey(on_delete=models.CASCADE)
    # SET 에 함수로 
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bid')
    bid_price = models.IntegerField()
    bid_time = models.DateTimeField(auto_now_add=True)
    # bid_status
    def __str__(self):
      return self.product_id.title
    
    class Meta:
      ordering = ['-bid_time']


class Comment(models.Model):
    # user_id = models.ForeignKey(on_delete=models.SET())
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.product_id,  self.content