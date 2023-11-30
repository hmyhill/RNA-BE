from decimal import MAX_EMAX
from django.db import models
from django.contrib.auth.models import User

#Setting choice variables for dropdown lists
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

TAGS = (
    (0, "---"),
    (1, "Entertainment"),
    (2, "Sport")
    )

#Setting the database models to store article data
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    tags = models.IntegerField(choices=TAGS, default = 0)

    def __str__(self):
        return self.title
