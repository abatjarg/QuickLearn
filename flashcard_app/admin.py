from django.contrib import admin
from flashcard_app.models import Category, Card

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}


admin.site.register(Card)
admin.site.register(Category,CategoryAdmin)