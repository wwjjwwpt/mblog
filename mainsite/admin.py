from django.contrib import admin
from .models import Post,Post1,Post2,Post3,Post4
from .models import UserPass
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')



class UserPassAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Post,PostAdmin)
admin.site.register(Post1,PostAdmin)
admin.site.register(Post2,PostAdmin)
admin.site.register(Post3,PostAdmin)
admin.site.register(Post4,PostAdmin)
admin.site.register(UserPass,UserPassAdmin)