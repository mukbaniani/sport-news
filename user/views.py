from .forms import UserRegister
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Account
from post.models import Post
from django.db.models import Count


class RegisterView(CreateView):
    model = Account
    template_name = "user/register.html"
    form_class = UserRegister


class UserDetailView(DetailView):
    model = Account
    template_name = 'user/account.html'
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        stat_info = Post.objects.filter(user_id=self.request.user.id).aggregate(posts=Count('user'), comments=Count('comment'))
        context.update({'stat_info': stat_info})
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Account
    template_name = 'user/update.html'
    fields = ['username', 'email', 'image']

    def test_func(self):
        account = self.get_object()
        return self.request.user == account