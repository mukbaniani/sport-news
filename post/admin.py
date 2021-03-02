from django.contrib import admin
from .models import League, Team, Post, Comment


class InlineTeam(admin.TabularInline):
    model = Team


class CommemtAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'user')
    list_filter = [('user')]
    search_fields = ['user__username']


class LeagueAdmin(admin.ModelAdmin):
    inlines = [InlineTeam]
    fields = ("leagues", "image")
    list_display = [('leagues')]
    search_fields = [('leagues')]


class PostListFilter(admin.SimpleListFilter):
    title = 'დასადასტურებელი პოსტები'
    parameter_name = 'see_home_page'

    def lookups(self, request, model_admin):
        return (
            ("Yes", 'დადასტურებული პოსტები'),
            ("No", 'დასადასტურებელი პოსტები')
        )

    def queryset(self, request, queryset):
        if self.value() == "No":
            return queryset.filter(see_home_page=False)
        if self.value() == "Yes":
            return queryset.filter(see_home_page=True)


class PostAdmin(admin.ModelAdmin):
    exclude = [('user')]
    list_display = ('user', 'title', 'league', 'team')
    search_fields = ['user__username', 'title', 'team__teams', 'league__leagues']
    list_filter = (PostListFilter,)
    list_editable = ('league', 'team')
    list_per_page = 1
    list_display_links = ('user', 'title')


admin.site.register(League, LeagueAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommemtAdmin)