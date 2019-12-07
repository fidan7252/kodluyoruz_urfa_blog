from django.shortcuts import render
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
    context['item'] = Post.objects.get(
        slug=post_slug
    )
    context['item'].user_viewed()
    # context['item'] = Post.objects.get(slug=post_slug)
    return render(request, 'blog/post.html', context)