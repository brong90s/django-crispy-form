from django.shortcuts import render

from .forms import BasicForm

def signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BasicForm()
    return render(request, 'signup.html', {'form': form})
