from django.contrib import admin

# Register your models here.
from .models import Product,ProductImage

class ProductAdmin(admin.ModelAdmin):
    search_fields=['title','description']
    list_display = ['__str__','title','price','active','updated']
    list_editable = ['price','active']
    list_filter = ['price','active']
    date_hierarchy = 'timestamp'
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)
