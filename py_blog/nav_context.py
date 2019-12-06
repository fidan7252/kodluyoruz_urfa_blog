from blog.models import Category
# py_blog/nav_context.py
# context_processor

def navbar(request):
    return {
        'categories': Category.objects.filter(
            status="published"
        )
    }