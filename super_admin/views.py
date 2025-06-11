from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
# from users.models import Profile
from news.models import Category
from news.models import Tag
from news.models import Article
from news.models import Banner
# from functions.decorations import allow_access_to
from django.contrib.auth import get_user_model
User = get_user_model()

# @allow_access_to([User.USER_TYPE_SUPER_ADMIN])
def super_admin_dashboard_view(request):
    user = User.objects.get(id=pk)
    if request.method=='POST':
        data = request.POST
        username = data.get("username")
        fn = data.get("firstname")
        ln = data.get("lastname")
        eml = data.get("email ")
        mob = data.get("mobile")
        profile_pic=request.FILES.get("profile_pic")
        user.username=username
        user.first_name=fn
        user.last_name=ln
        user.email=eml
        user.save()
        user=User.objects.get(user=user)
        user.mobile=mob
        if profile_pic:
            pr.profile_pic=profile_pic
            user.save()
    return render(request, "dashboard/profile.html")
    
def super_admin_dashboard_view(request):
  return render(request, "dashboard/dashboard.html")

def super_admin_profile_view(request):
    return render(request, 'dashboard/profile.html')

def super_admin_password_change_view(request):
    return render(request, "dashboard/users/password_change.html")

def super_admin_user_list_view(request):
    users = User.objects.all()
    return render(request, "dashboard/users/user_list.html", {'users': users})

def super_admin_user_detail_view(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "dashboard/users/user_detail.html",{'user':user})

def super_admin_user_create_view(request):
    if request.method == 'POST':
        data = request.POST
        un = data.get("username")
        eml = data.get("email")
        fn = data.get("firstname")
        ln = data.get("lastname")
        mb = data.get("mobile")
        pw = data.get("password")
        cpsw = data.get("confirmpassword")
        user = User.objects.create_user(username=un, email=eml, first_name=fn, last_name=ln, password=pw, mobile=mb)
        # User.objects.create(user=user, mobile=mb)
        messages.success(request, "Your account has been created successfully.")
    return render(request,  "dashboard/users/user_create.html")

def super_admin_user_update_view(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        un = data.get('username')
        em = data.get('email')
        fn = data.get('first_name')
        ln = data.get('last_name')
        mn = data.get('mobile')
        
        user.username=un
        user.email=em
        user.first_name=fn
        user.last_name=ln
        user.profile.mobile=mn
        user.save()
    return render(request, "dashboard/users/user_update.html",{'user':user})

def super_admin_user_delete_view(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect("/super_admin/user-list/")

def super_admin_user_activate_view(request, pk):
    user = get_object_or_404(User, id=pk)
    user.is_active=True
    user.save()
    return redirect("/super_admin/user-list/")

def super_admin_user_dactivate_view(request, pk):
    user = get_object_or_404(User, id=pk)
    user.is_active=False
    user.save()
    return redirect("/super_admin/user-list/")

def super_admin_category_list_view(request):
    categories = Category.objects.all()
    return render(request, "dashboard/news/category_list.html", {'categories': categories})

def super_admin_category_create_view(request):
    if request.method=='POST':
        data = request.POST
        nm = data.get("name")
        des = data.get("description")
        ac = data.get("is_active")
        img = request.FILES.get("featured_image")
        Category.objects.create(name=nm, description=des, is_active=(True if ac=='on' else False), featured_image=img)
    return render(request, "dashboard/news/category_create.html")

def super_admin_category_update_view(request, pk):
    news = Category.objects.get(id=pk)
    if request.method=='POST':
        data = request.POST
        nm = data.get("name")
        des = data.get("description")
        ac = data.get("is_active")
        img = request.FILES.get("featured_image")
        news.name=nm
        news.description=des
        news.is_active=ac=(True if ac=='on' else False)
        if img:
           news.featured_image=img
        news.save()
    return render(request, "dashboard/news/category_update.html",{'news':news})

def super_admin_category_detail_view(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "dashboard/news/category_details.html",{'category': category})

def super_admin_category_delete_view(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect("/super_admin/category-list/")

def super_admin_tag_list_view(request):
    tags = Tag.objects.all()
    return render(request, "dashboard/news/tag_list.html",{'tags':tags})
    
def super_admin_tag_create_view(request):
    if request.method=='POST':
        data = request.POST
        nm = data.get("name")
        des = data.get("description")
        img = request.FILES.get("featured_image")
        fea= data.get("is_featured")
        Tag.objects.create(name=nm, description=des,featured_image=img, is_featured=(True if fea=='on' else False))
    return render(request, "dashboard/news/tag_create.html")

def super_admin_tag_update_view(request, pk):
    tag=Tag.objects.get(id=pk)
    if request.method=="POST":
        data = request.POST
        nm = data.get("name")
        des = data.get("description")
        img = request.FILES.get("image")
        is_featured = data.get("is_featured")
        tag.name=nm
        tag.description=des
        tag.is_featured= (True if is_featured=="on" else False)
        if img:
            tag.featured_image=img
        tag.save()
    return render(request,"dashboard/news/tag_update.html",{'tag':tag})


def super_admin_tag_delete_view(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect("/super_admin/tag-list/")

def super_admin_tag_details_view(request, pk):
    tag = Tag.objects.get(id=pk)
    return render(request, "dashboard/news/tag_details.html",{'tag':tag})

def super_admin_article_list_view(request):
    articles = Article.objects.all()
    return render(request, "dashboard/news/article_list.html",{'articles':articles})

def super_admin_article_create_view(request):
    if request.method=="POST":
        data = request.POST
        title = data.get("title")
        content = data.get("content")
        cat_id = data.get("category")
        tags = data.get("tags")
        status = data.get("status")
        # category = Category.objects.get(id=cat_id)
        # Article.objects.create(title=title, content=content, category=category, status=status)
        Article.objects.create(title=title, content=content, category_id=cat_id, status=status)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        "categories": categories, 
        "tags": tags,
        "status_choices": Article.STATUS_CHOICES,
    
        }
    return render(request,"dashboard/news/article_create.html",context)

def super_admin_article_update_view(request, pk):
    article=Article.objects.get(id=pk)
    if request.method=='POST':
        data = request.POST
        title = data.get("title")
        content = data.get("content")
        cat_id = data.get("category") 
        tag_ids= data.getlist("tags")
        status = data.get("status")
        is_breaking = data.get("is_breaking")
        is_trending = data.get("is_trending")
        is_featured = data.get("is_featured")
        is_sponsored = data.get("is_sponsored")
        allow_comments = data.get("allow_comments")
        reading_time = data.get("reading_time")
        
        article.title = title
        article.content = content
        article.category_id = cat_id
        article.status = status
        article.is_breaking = (True if is_breaking=='on' else False)
        article.is_trending = (True if is_trending=='on' else False)
        article.is_featured= (True if is_featured=='on' else False)
        article.is_sponsored = (True if is_sponsored=='on' else False)
        article.allow_comments = (True if allow_comments=='on' else False)
        if reading_time and reading_time.strip():
         article.reading_time = reading_time.strip()
        article.save()


    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
    "categories": categories, 
    "tags": tags,
    "status_choices": Article.STATUS_CHOICES,
    "article": article
    }
    article.save()
    return render(request, "dashboard/news/article_update.html",context)

def super_admin_article_detail_view(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "dashboard/news/article_details.html",{'article': article})
    

def super_admin_article_delete_view(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect("/super_admin/article-list/")

def super_admin_article_status_update_view(request, pk):
    pass

def super_admin_article_publish_view(request, pk):
    pass
    
def super_admin_article_unpublish_view(request, pk):
    pass


def super_admin_banner_list_view(request):
    banners = Banner.objects.all()
    return render(request, "dashboard/news/banner_list.html",{'banners':banners})

def super_admin_banner_create_view(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get("title")
        content = data.get("content")  
        link = data.get("link")
        order = data.get("order")
        image = request.FILES.get("featured_image")
        is_active = data.get("is_active") == "on" 
        created_at = data.get("created_at")
        Banner.objects.create( title=title,content=content,image=image,link=link,is_active=is_active, order=order,created_at=created_at)
    return render(request,"dashboard/news/banner_create.html")

def super_admin_banner_update_view(request, pk):
    banner=Banner.objects.get(id=pk)
    if request.method=='POST':
        data = request.POST
        title = data.get("title")
        content = data.get("content")
        link = data.get("link")
        order = data.get("order")
        image = request.FILES.get("featured_image")
        is_active = data.get("is_active") == "on" 
        created_at = data.get("created_at")
        banner.title=title
        banner.content=content
        banner.link=link
        banner.order=order
        banner.image=image
        banner.is_active=is_active
        banner.created_at=created_at
        banner.save()
    return render(request, "dashboard/news/banner_update.html", {'banner': banner})


def super_admin_banner_detail_view(request, pk):
     banner = Banner.objects.get(id=pk)
     return render(request, "dashboard/news/banner_details.html",{'banner':banner})

def super_admin_banner_delete_view(request, pk):
    banner = Banner.objects.get(id=pk)
    banner.delete()
    return redirect("/super_admin/banner-list/")
