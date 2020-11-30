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


class Post(models.Model):
    choices = (
        ("Adventure", "Adventure"),
        ("Blog", "Blog"),
        ("Photography", "Photography"),
        ("Culture", "Culture"),
        ("Tv", "Tv"),
        ("Fashion", "Fashion"),
        ("Lifestyle", "Lifestyle"),
        ("Life", "Life"),
        ("God", "God"),
        ("Movies", "Movies"),
        ("Culture", "Culture"),
        ("Weather", "Weather"),
        ("Art", "Art"),
        ("Space", "Space"),
        ("Nature", "Nature"),
        ("Computer", "Computer"),
        ("SocialMedia", "SocialMedia"),
    )
    title = models.CharField(max_length=400)
    tags = models.CharField(max_length=255, default='AddTags')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.localtime())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='AddCategory', choices=choices)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    dislikes = models.ManyToManyField(User, related_name="blog_posty")

    def total_likes(self):
        return self.likes.count()

    def total_dislike(self):
        return self.dislikes.count()

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
