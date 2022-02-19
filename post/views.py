from django.urls.base import reverse
from .forms import CommentForm
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Team
from .utils import MainPostView, MainDelete



class PostListView(MainPostView):
    template_name = "post/home.html"

    def get_queryset(self):
        return Post.objects.filter(see_home_page=True)


class FilterByLeague(MainPostView):
    template_name = "post/filter-by-league.html"

    def get_queryset(self):
        return Post.objects.filter(league_id=self.kwargs['pk']).filter(see_home_page=True)

    def get_context_data(self, **kwargs):
        context = super(FilterByLeague, self).get_context_data(**kwargs)
        context.update({"teams": Team.objects.all()})
        return context


class FilterByTeam(MainPostView):
    template_name = "post/filter-by-team.html"

    def get_queryset(self):
        return Post.objects.filter(team_id=self.kwargs['pk']).filter(see_home_page=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "post/show.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        same_posts = Post.objects.filter(league=self.object.league, id__gte=self.object.id + 1).order_by('-id')[:10]
        context.update({"form": CommentForm, "comments": self.object.comment_set.all(), "same_posts": same_posts})
        return context


class CommentView(CreateView):
    model = Comment
    fields = ["comment"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show-detail', kwargs={"pk": self.object.post.id})


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/create-post.html"
    fields = ["title", "short_desc", "desc", "image", "league", "team"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.user.is_superuser:
            form.instance.see_home_page = True
        return super().form_valid(form)


class DeleteComment(MainDelete):
    model = Comment
    
    def get_success_url(self):
        return reverse('show-detail', kwargs={"pk": self.object.post.id})


class DeletePost(MainDelete):
    model = Post
    
    def get_success_url(self):
        return reverse('home-page')