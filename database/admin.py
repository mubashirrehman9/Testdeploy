from django.contrib import admin
from .models import Product, Subcategory, Category, Contact, Profile, Review, ProductImage, ProductDiscription, \
    AditionalInform

admin.site.register(Product),
admin.site.register(Subcategory),
admin.site.register(Category),
admin.site.register(Contact),
admin.site.register(Review),
admin.site.register(ProductImage),
admin.site.register(ProductDiscription),
admin.site.register(AditionalInform),


class Newprofile(admin.ModelAdmin):
    list_display = ['id', 'user', 'token', 'verify']


admin.site.register(Profile, Newprofile),
