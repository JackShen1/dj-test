import json

from .forms import TestForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_requests(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            output = json.dumps(form.cleaned_data, indent=4)
            content = {
                'form': form,
                'json_response': output,
                'status': 'HTTP 201 Created',
            }
            return render(request, 'my_form.html', content, status=201)
        else:
            output = json.dumps(dict(form.errors.items()), indent=6)
            content = {
                'form': form,
                'json_response': output,
                'status': 'HTTP 400 Bad Request',

            }
            return render(request, 'my_form.html', content, status=400)

    else:
        form = TestForm()

    return render(request, 'my_form.html', {'form': form})
