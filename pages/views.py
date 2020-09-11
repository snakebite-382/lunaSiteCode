from django.shortcuts import render

# Create your views here.
def contact_view(request):
	return render(request, 'pages/contact.html', {})

def about_view(request):
	return render(request, 'pages/about.html', {})
