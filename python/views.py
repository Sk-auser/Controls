from django.shortcuts import render, redirect

from .forms import NumberForm

def index(request):
    form = NumberForm()  # Create an instance of the form
    return render(request, 'python/index.html', {'form': form})

def calculate_average(request):

    numbers = request.session.get('numbers', [])

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            numbers.append(number)
            request.session['numbers'] = numbers  # Store numbers in session
            if len(numbers) >= 5:  # Check if 5 numbers have been entered
                total = sum(numbers)
                average = total / len(numbers)
                del request.session['numbers']  # Reset the stored numbers
                return render(request, 'python/index.html', {'average': average, 'numbers': numbers, 'form': NumberForm()})
    else:
        form = NumberForm()
    return render(request, 'python/index.html', {'form': form, 'numbers': numbers})

