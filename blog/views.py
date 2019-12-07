from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Post


def index(request, cat_slug=None):
    context = dict()
    # context['categories'] = Category.objects.filter(
    #     status='published'
    # ).order_by('title')
    context['items'] = Post.objects.filter(
        status='published'
    ).order_by('-created_at')
    if cat_slug:
        category = Category.objects.get(slug=cat_slug)
        context['category'] = category
        category.user_viewed()
        context['items'] = context['items'].filter(
            category=category
        )
    return render(request, 'index.html', context)


# def category(request, cat_slug):
#     context = dict()
#     category = Category.objects.get(slug=cat_slug)
#     context['category'] = category
#     context['categories'] = Category.objects.filter(
#         status='published'
#     ).order_by('title')
#     context['items'] = Post.objects.filter(
#         category=category,
#         status='published'
#     ).order_by('-created_at')
#     return render(request, 'index.html', context)



def post_detail(request, cat_slug, post_slug):
    context = dict()
    item = Post.objects.get(
        slug=post_slug
    )
    context['item'] = item
    item.user_viewed()
    # print(context['item'].category.user_viewed())
    # context['item'] = Post.objects.get(slug=post_slug)
    return render(request, 'blog/post.html', context)


def add_category(request):
    if request.method == "POST":
        if request.user.is_staff:
            r_post = request.POST
            title = r_post.get('title')
            try:
                item = Category.objects.create(
                    title = title, slug = title,
                )
                messages.add_message(
                    request, messages.SUCCESS, f'{title} Kaydedildi'
                )
                if request.user.is_superuser:
                    item.status = "published"
                    item.save()
                    messages.add_message(
                        request, messages.SUCCESS, f'{title} Yayinlandi'
                    )
                return redirect('home')
            except:
                messages.add_message(
                    request, messages.WARNING, 
                    f'{title} Kaydedilemedi'
                )

    return render(request, 'blog/add_category.html', {})



def category_list(request):
    context = dict()
    categories = Category.objects.all()
    context = {
        'categories_list': categories,
        'is_super': request.user.is_superuser
    }
    return render(request, 'blog/categories.html', context)


def category_update_status(request, category_id, status):
    instance = Category.objects.get(id=category_id)
    instance.status = status
    instance.save()
    messages.add_message(request, messages.SUCCESS, 
        f"{instance.title} Silindi"
    )
    return redirect('category_list')