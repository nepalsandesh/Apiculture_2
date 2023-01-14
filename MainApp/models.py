from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args,**kwargs)
        

    def __str__(self):
        return str(self.author)+ ", Blog Title: " + str(self.title)

    def get_absolute_url(self):
        return reverse('blogs')


    def get_all_likes_number(self):
        all_likes = self.likes.all()
        return all_likes.count()

    def get_all_comments_number(self):
        all_comments = Comment.objects.filter(blog=self).all()
        return all_comments.count()


class Comment(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    DateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + ", Comment: " + self.content

class Message(models.Model):
    sender = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sender

