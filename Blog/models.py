from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')


class Post(models.Model):
    choices = (
        ("Adventure", "Adventure"),
        ("Culture", "Culture"),
        ("Entertainment & Pop Culture", "Entertainment & Pop Culture"),
        ("Fashion", "Fashion"),
        ("Geography & Travel", "Geography & Travel"),
        ("Health & Medicine", "Health & Medicine"),
        ("Literature", "Literature"),
        ("Lifestyle", "Lifestyle"),
        ("Movies", "Movies"),
        ("Nature", "Nature"),
        ("Photography", "Photography"),
        ("Philosophy & Religion", "Philosophy & Religion"),
        ("Politics, Law & Government", "Politics, Law & Government"),
        ("Science", "Science"),
        ("Social Issues", "Social Issues"),
        ("Space", "Space"),
        ("Sports & Recreation", "Sports & Recreation"),
        ("Technology", "Technology"),
        ("Visual Arts", "Visual Arts"),
        ("World History", "World History"),

    )
    title = models.CharField(max_length=400)
    tags = models.CharField(max_length=255, default='AddTags')
    content = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="")
    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='AddCategory', choices=choices)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    dislikes = models.ManyToManyField(User, related_name="blog_postss")

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
