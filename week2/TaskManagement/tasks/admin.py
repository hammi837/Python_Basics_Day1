from django.contrib import admin
from .models import Task, Category

# Register your models so admin can manage them
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'due_date', 'completed')
    list_filter = ('category', 'completed')
    search_fields = ('title', 'owner__username')
    ordering = ('due_date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




