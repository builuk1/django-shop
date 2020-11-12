from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Order
from .models import Product
from .models import Feedback
from .models import Gallery
from django.views.generic import ListView

# Create your views here.
# class HomePageView(ListView):
#     model = Feedback
#     template_name = 'home.html'

def home(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    gallery = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'shop/home.html', {'feedbacks': feedbacks,'gallery': gallery})


