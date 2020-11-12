from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

#Post Example
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Feedback Example
class Feedback(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Product Example
class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=200)
    text1 = models.TextField()
    title2 = models.CharField(max_length=200)
    text2 = models.TextField()
    title3 = models.CharField(max_length=200)
    text3 = models.TextField()
    title4 = models.CharField(max_length=200)
    text4 = models.TextField()
    title5 = models.CharField(max_length=200)
    text5 = models.TextField()
    title6 = models.CharField(max_length=200)
    text6 = models.TextField()
    title7 = models.CharField(max_length=200)
    text7 = models.TextField()
    size1 = models.TextField()
    size2 = models.TextField()
    size3 = models.TextField()
    size4 = models.TextField()
    size5 = models.TextField()
    color1 = models.TextField()
    color2 = models.TextField()
    color3 = models.TextField()
    color4 = models.TextField()
    color5 = models.TextField()
    cover1 = models.ImageField(upload_to='images/')
    cover2= models.ImageField(upload_to='images/')
    cover3 = models.ImageField(upload_to='images/')
    cover4 = models.ImageField(upload_to='images/')
    cover5 = models.ImageField(upload_to='images/')
    cover6 = models.ImageField(upload_to='images/')
    cover7 = models.ImageField(upload_to='images/')
    cover8 = models.ImageField(upload_to='images/')
    cover9 = models.ImageField(upload_to='images/')
    cover10 = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Order Example
class Order(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    phone = models.TextField()
    size = models.TextField()
    color = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
