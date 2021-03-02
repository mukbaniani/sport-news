from django.db import models
from django.urls import reverse
from user.models import Account
from PIL import Image

class League(models.Model):
    leagues = models.CharField(max_length=100, verbose_name='ჩემპიონატის სახელი', unique=True)
    image = models.ImageField(verbose_name='ჩემპიონატის ლოგო', upload_to='images')

    def __str__(self):
        return self.leagues

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        verbose_name_plural = "ჩემპიონატები და გუნდები"


class Team(models.Model):
    teams = models.CharField(max_length=70, unique=True, verbose_name='გუნდის სახელი')
    image = models.ImageField(verbose_name='გუნდის ლოგო', upload_to='images')
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='ჩემპიონატი, რომელშიც გუნდი თამაშობს')

    def __str__(self):
        return self.teams

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='სათაური')
    short_desc = models.TextField(verbose_name='მოკლე აღწერა')
    desc = models.TextField(verbose_name='აღწერა')
    see_home_page = models.BooleanField(default=False, verbose_name='დადასტურება')
    image = models.ImageField(verbose_name='სურათი', upload_to='images')
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='ჩემპიონატი')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='გუნდი')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='სიახლის ავტორი')

    def  __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-page')

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        verbose_name_plural = "სიახლეები"
        ordering = ['-id']


class MainComment(models.Model):
    comment = models.TextField(verbose_name='კომენტარი')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='პოსტი')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='კომენტრის ავტორი')

    
    class Meta:
        abstract = True
 

class Comment(MainComment):
    def __str__(self):
        return self.comment


    class Meta:
        verbose_name_plural = "პოსტის კომენტარები"


class ReplyComment(MainComment):
    reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment