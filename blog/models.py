from django.db import models
from django.urls import reverse


STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

DEFAULT_STATUS = "draft"

class Category(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(
        max_length=200, 
        blank=True, 
        unique=True,
    )
    viewed = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=DEFAULT_STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def user_viewed(self):
        self.viewed += 1
        self.save()
        return f"{self.viewed}"

    def get_absolute_url(self):
        # return f"/category/{self.slug}/"
        # /category/self.slug/
        return reverse(
            'cat', 
            kwargs={'cat_slug':self.slug }
        )

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(
        max_length=200, 
        blank=True, 
        unique=True,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=DEFAULT_STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(
        max_length=200, 
        blank=True, 
        unique=True,
    )
    content = models.TextField(null=True)
    cover_image = models.ImageField(upload_to='post', blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=DEFAULT_STATUS,
    )
    viewed = models.PositiveIntegerField(default=0)
    is_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def user_viewed(self):
        self.viewed += 1
        self.save()
        return f"{self.viewed}"

    def get_tags_in_a(self):
        return self.tags.filter(
            title__icontains='a'
        )
    
    def get_latest_posts(self):
        latest_posts = Post.objects.filter(
            category=self.category,
            status="published"
        ).exclude(id=self.id)[:5]
        return latest_posts
    
    def get_absolute_url(self):
        # return f"/category/{self.slug}/"
        # /category/self.slug/
        return reverse(
            'post_detail',  #urls.py
            kwargs={
                'cat_slug': self.category.slug,
                'post_slug': self.slug 
            }
        )

    def __str__(self):
        return self.title


# item in kendi kategorisindeki son 5,
# kendisi haric
