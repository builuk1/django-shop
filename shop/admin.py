from django.contrib import admin
from django.contrib import admin
from .models import Post
from .models import Product
from .models import Order
from .models import Feedback
from .models import Gallery

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(Gallery)
# Register your models here.
