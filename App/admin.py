from django.contrib import admin
from .models import Post_New
from .models import Post_Discount
from .models import Post_Milk
from .models import Post_Soda
from .models import Post_Smoothies
from .models import Post_Recommended
from .models import Post_List
from .models import Post_Cart

# Register your models here.

admin.site.register(Post_New)
admin.site.register(Post_Discount)
admin.site.register(Post_Milk)
admin.site.register(Post_Soda)
admin.site.register(Post_Smoothies)
admin.site.register(Post_Recommended)
admin.site.register(Post_List)
admin.site.register(Post_Cart)
