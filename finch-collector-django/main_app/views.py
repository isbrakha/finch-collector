from django.shortcuts import render


finches = [
       {'name': 'Marcus Aurelius', 'breed': 'Golden Finchtreiver', 'description': 'Smart and cute', 'age': 3},
       {'name': 'Jennifer', 'breed': 'Evening grosebeak', 'description': 'Likes to fly', 'age': 2},
       {'name': 'Lewis', 'breed': 'Purple Finch', 'description': 'Is red', 'age': 4},
       
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
          return render(request, 'about.html')

def finches_index(request):
       return render(request, 'finches/index.html', {
              'finches' : finches
       })