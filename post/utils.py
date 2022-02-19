from django.views.generic import ListView, DeleteView
from .models import Post
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class MainPostView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = ['-id']


class MainDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "post/delete.html"

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user or self.request.user.is_superuser    