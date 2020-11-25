from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')


# choices = ['Life', 'Work', 'Happiness', 'Exercise', 'God', 'Entertainment', 'Science', 'Computers', 'Family',
# 'Social ' 'Media', 'Fashion', 'Food', 'Lifestyle', 'Photography', 'Nature', 'Travel', 'others']

choices = Category.objects.all().values_list('name')
choice_list = []

for item in choices:
    choice_list.append(item)


class Post(models.Model):
    title = models.CharField(max_length=400)
    tags = models.CharField(max_length=255, default='AddTags')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='AddCategory', choices=choice_list)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    Text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    # The related_name attribute allows us to name the attribute that we use for the relation from the related object
    # back to this one we have a Foreign key relation that establishes a many-to-one relationship with the Post
    # model, since every comment will be made on a post and each post will have multiple comments.

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.Text, self.name)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.post.id})
