from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator #페이지네이터 임포트
from .models import Blog    #데이터베이스 임포트
from .forms import BlogForm

# Create your views here.
# all get order_by filter exclude

def home(request):
    # blogs = Blog.objects.all() #블로그 테이블의 객체들을 긁어와라
    blogs = Blog.objects.order_by('-pub_date') #-빼면 얘전 글부터 나타남(시간 순, 시간 역순)
    search = request.GET.get('search')
    if search == 'true': #특정 작성자가 게시한것만 찾아주는 기능
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer = author)    #filter를 exclude로 바꿔주면 작성자를 제외한 글만 나옴(뒤에 order_by붙일수 있다)
        return render(request,'home.html',{'blogs':blogs})
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,id): #path-converter
    blog = get_object_or_404(Blog, pk = id)  #찾을 수 없는 페이지 요청시 404에러창 표시?
                                        #갖고올 테이블인 Blog와 pk(primary key : db 테이블에서 행 구분자인 ID와 같다)를 인자로 받음
    return render(request,'detail.html',{'blog':blog})

def new(request):
    form = BlogForm()   #선언
    return render(request, 'new.html', {'form' : form})  #Create 기능 함수, form 객체를 그대로 넘겨줌

def create(request):    #입력받고 데이터베이스를 생성하는 함수
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():   #유효성 검사
        new_blog = form.save(commit=False)  #임시저장
        new_blog.pub_date = timezone.now()  #시간
        new_blog.save()
        return  redirect('detail', new_blog.id) #새로만든 원래 페이지로 돌아감
    return redirect('home') #실패시 홈으로

def edit(request, id):  #edit.html 보여주는 함수 : 수정시 기존 데이터테이블을 보여주는 기능 구현(인자 id 이용)
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request,id): #수정한걸 update! 데이터베이스에 적용시키는 함수 -> 수정할 데이터의 id값을 받아야한다는 점에서 create와 다름
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()  #데이터베이스에 저장!
    return redirect('detail', update_blog.id)

def delete(request, id):    #삭제 코드~~
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')
