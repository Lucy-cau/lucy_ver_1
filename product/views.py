from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone

# 스플래쉬 화면
def splash(request):
    return render(request, 'splash.html')
# 홈페이지
def home(request):

    #  DB로부터 데이터를 가져와 render의 3번째 인자로 딕셔너리형태로 index.html에 업데이트

    # QuerySet : 데이터베이스로부터 전달받은 객체 목록
    # QuerySet 에 담긴 객체를 가져다 쓰려면 for문으로   

    # DB에 담긴 데이터 전부 가져오기
    products = Product.objects.all()

    print(products)
    # deadline = products.register_time + timedelta(hours=24)

    # DB로부터 필터링해서 데이터 가져오기. 참고로 '-'는 역순으로 정렬
    # posts = Blog.objects.filter().order_by('-date')
    
    return render(request, 'index.html', {'products':products})


# 상세페이지 보여지도록 하는 함수 ; 어떤 데이터를 넘겨줄지 정의하는 부분
# url path 정의할 때 blog_id 변수 가져옴.
def detail(request, product_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 가져와서
    # Blog 객체를 가져올 건데 pk값이 blog_id인 객체를 가져올 거야. 
    product_detail = get_object_or_404(Product, pk=product_id)

    # 댓글 입력 폼
    comment_form = CommentForm()
    # blog_id 번째 블로그 글을 detail.html 로 띄워주는 코드
    return render(request, 'detail.html', {'product_detail': product_detail, 'comment_form':comment_form})

# 입찰 페이지
def bid(request):
    return render(request, 'bid.html')


# model form으로 만들어진 form은 models.py에서 정의한 모델을 기반으로 만들어져 자체적으로 save 메서드를 갖고 있다.
# 반면 django form 으로 만들어진 form은 models.py에서 정의한 객체를 만들고 값을 넣어준 다음 그 객체에서 save해줘야함.
def productformcreate(request):
    # post 요청
    if (request.method == 'POST' or request.method == 'FILES'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    # get요청 ; 모델 폼 틀 보여줌.
    else:
        form = ProductForm()
    
    # 'form_create.html' 그대로 사용해도 상관없음.
    return render(request, 'formcreate.html', {'form': form})


# 사용자가 작성한 댓글을 저장하는 함수
def create_comment(request, product_id):
    # POST형식으로 들어온 요청을 처리
    filled_form = CommentForm(request.POST)

    # 사용자가 작성한 댓글이 유효하다면 저장.
    if filled_form.is_valid():
        # 근데 주의. 저장하기 전에 어떤 글의 댓글인지 알기 위한 blog_id도 함께 저장해야함.
        # -> 아직 저장하지 않고 대기
        finished_form = filled_form.save(commit=False)
        # -> 어떤 글에 대한 댓글인지 CommentForm 의 post 정보 입력
        finished_form.product_id = get_object_or_404(Product, pk=product_id)
        # -> 그 다음 저장.
        finished_form.save()

    return redirect('detail', product_id)


def productformcreate(request):
    # post 요청
    if (request.method == 'POST'):
      form = ProductForm(request.POST)
      if form.is_valid():
        filled_form = form.save(commit=False)
        I = range(1, 5)
        i = 1
        for i in I:
          b = Locker.objects.get(id = i)
          if b.locker_status ==  0:
            break
          i = i+1
        filled_form.locker = b
        filled_form.save()
      filled_locker = Locker.objects.get(id = i)
      filled_locker.locker_status = 1
      filled_locker.save()
      return render(request, 'product_check.html', {'filled_locker':filled_locker})

    # get요청 ; 모델 폼 틀 보여줌.
    else:
        form = ProductForm()
  
    return render(request, 'formcreate.html', {'form': form})


# 바로구매 확정페이지로 렌더링하는 함수
def purchase(request, product_id):
    # get요청 ; 모델 폼 틀 보여줌.
    product_info = get_object_or_404(Product, pk=product_id)    

    return render(request, 'confirm_purchase.html',{'product_info': product_info})

def bidformcreate(request, product_id):
    # post 요청
    # if (request.method == 'POST'):
    #     form = BidForm(request.POST)
    #     if form.is_valid():  
    #         form.save()
    #         return redirect('detail', product_id)
    
    # get요청 ; 모델 폼 틀 보여줌.
    if (request.method == "GET"):
        # 상품정보 불러오기 위해 product 객체 가져옴.
        product_info = get_object_or_404(Product, pk=product_id)
        # 입력폼
        form = BidForm()

    # 'form_create.html' 그대로 사용해도 상관없음.
    return render(request, 'bid.html', {'form': form, 'product_info': product_info})


# 사용자가 작성한 입찰정보를 저장하는 함수
def create_bid(request, product_id):
    # POST형식으로 form에 입력된 요청을 처리
    filled_form = BidForm(request.POST)

    # 사용자가 작성한 댓글이 유효하다면 저장.
    if filled_form.is_valid():
        # 근데 주의. 저장하기 전에 어떤 글의 댓글인지 알기 위한 blog_id도 함께 저장해야함.
        # -> 아직 저장하지 않고 대기
        finished_form = filled_form.save(commit=False)
        # for 문으로 돌려야하나?
        # for i in 1:
        #     a = 1
        # bid = get_object_or_404(Bid, pk=1)
        
        # 이전 bid객체의 bid_price 보다 높은 가격일 때 저장
        if finished_form.bid_price > 123:

            # -> 어떤 상품에 대한 입찰인지 BidForm 의 post 정보 입력
            finished_form.product_id = get_object_or_404(Product, pk=product_id)
            # -> 그 다음 저장.
            finished_form.save()
            print('굳굳')

        else:
            print('다시 입력필요')
    return redirect('detail', product_id)

# 사용자가 작성한 바로구매정보를 저장하는 함수
def create_purchase(request, product_id):
    # POST요청 처리 ; 바로구매 정보 담김
    if (request.method =="POST"):
        product_info = get_object_or_404(Product, pk=product_id)
        # Bid 객체 생성
        Bid.objects.create(
            product_id = product_info,
            bid_price = product_info.buyout_price,
            bid_time = timezone.now()
        )
        # product_info = Product.objects.filter(pk=product_id)
        # print(bid)
        # 상품 id
        # bid.product_id = 1
        # 즉시구매가
        # bid.bid_price = product_info.buyout_price
        # 입찰 시간
        # bid.bid_time = timezone.now()

        # 저장
        # bid.save()
    
    # render는 같은 url안에 렌더링만 바꿔줌. redirect는 url 바꿔줌.
    # redirect 는 url name만 적어줘도 됨.
    return render(request, 'buy_locker_check.html', {'product_info':product_info})


    # filled_form = BidForm(request.POST)

    # # 사용자가 작성한 댓글이 유효하다면 저장.
    # if filled_form.is_valid():
    #     # 근데 주의. 저장하기 전에 어떤 글의 댓글인지 알기 위한 blog_id도 함께 저장해야함.
    #     # -> 아직 저장하지 않고 대기
    #     finished_form = filled_form.save(commit=False)
    #     # -> 어떤 글에 대한 댓글인지 CommentForm 의 post 정보 입력
    #     finished_form.product_id = get_object_or_404(Product, pk=product_id)
    #     # -> 그 다음 저장.
    #     finished_form.save()

    # return redirect('detail', product_id)