from django.shortcuts import render
from .models import Review
# Create your views here.
# def review_create_view(request):
#     form = ReviewForm(request.POST or None)
#     if form.is_valid():

#     return render

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        your_review = request.POST.get('your_review')
        email = request.POST.get('email')
        Review.objects.create(name=name, description=your_review, email=email)
        return render(request, 'review/thanks.html', {})
    #print(your_review)
    return render(request, 'review/index.html', {})