from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from .models import Comment, ReplyComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class RelpyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ["comment"]