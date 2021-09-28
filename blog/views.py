from django.core.paginator import Paginator
from siteSettings.models import SiteSettings
from django.contrib import messages
from comments.models import Comment
from django.shortcuts import render,redirect
from users.models import User
from .models import Blog

def blog_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()

            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')
        

    posts = Blog.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'وبلاگ'
    context = {
        'title': title,
        'posts': page_obj,
    }

    return render(request, 'blog/blog_page/blog.html', context)






def showBlog_page(request,slug):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    
    blog = Blog.objects.filter(slug__iexact=slug).first()
    Latest_blog = Blog.objects.all().order_by('-id')[:3]
    if request.method == "POST":
        username = request.user.username
        text = request.POST['text']

        user_info = User.objects.filter(username=username).first()
        comment_info = Comment.objects.filter(title=username).last()
        if comment_info is not None:
            if comment_info.status == True:
                comment = Comment.objects.create(title=username, slug=slug ,owner_id=request.user.id, text=text, image=user_info.user_photo, status=False)
                comments = Comment.objects.filter(status=True,slug=slug).all()
                messages.success(request,'دیدگاه شما با موفقیت ثبت شد و پس از تایید نمایش داده خواهد شد')
                context = {
                    'comments': comments,
                    'blog': blog,
                    'Latest_blog': Latest_blog,
                }

                return render(request, 'blog/showBlog_page/blog-single.html', context)

            else:
                comments = Comment.objects.filter(status=True,slug=slug).all()
                messages.error(request,'شما قبلا یک دیدگاه ثبت کرده اید , بعد از تایید دیدگاه میتونید دیدگاه جدیدی ثبت کنید')
                context = {
                    'comments': comments,
                    'blog': blog,
                    'Latest_blog': Latest_blog,
                }

                return render(request, 'blog/showBlog_page/blog-single.html', context)



        else:
            comment = Comment.objects.create(title=username, text=text, slug=slug , image=user_info.user_photo, status=False)
            comments = Comment.objects.filter(status=True,slug=slug).all()
            messages.success(request,'دیدگاه شما با موفقیت ثبت شد و پس از تایید نمایش داده خواهد شد')
            context = {
                'comments': comments,
                'blog': blog,
                'Latest_blog': Latest_blog,
            }

            return render(request, 'blog/showBlog_page/blog-single.html', context)


    else:
        comments = Comment.objects.filter(status=True,slug=slug).all()
        context = {
            'comments': comments,
            'blog': blog,
            'Latest_blog': Latest_blog,
        }

        return render(request, 'blog/showBlog_page/blog-single.html', context)
