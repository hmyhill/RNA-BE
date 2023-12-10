from decimal import MAX_EMAX
from django.db import models
from django.contrib.auth.models import User

#Setting choice variables for dropdown lists
TAGS = (
    (0, "---"),
    (1, "Entertainment"),
    (2, "Sport"),
    (3, "Technology"),
    (4, "World")
    )

#Setting the database models to store article data
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(default="")
    imageURl = models.TextField(default="")
    category = models.IntegerField(choices=TAGS, default=0)

    def __str__(self):
        return self.title
