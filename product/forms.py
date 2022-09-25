from django import forms
from .models import *


# 모델을 기반으로 한 model form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'start_price', 'buyout_price']
        # fields = '__all__'

# 댓글관련 model form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        # 데이터 모델짠 부분중에서 사용자한테 입력받을 부분.
        fields = ['content']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid

        # 데이터 모델짠 부분중에서 사용자한테 입력받을 부분.
        fields = ['bid_price']