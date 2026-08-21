from django.contrib import admin
from .models import Post, Comment, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('photo',)}),
    )


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']
    inlines = [CommentInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomUserAdmin)