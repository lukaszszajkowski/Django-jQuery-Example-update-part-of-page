# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.shortcuts import render


log_file = [
    "Wating ... 1",
    "Wating ... 2",
    "Wating ... 3",
    "Test 1 OK  4",
    "Wating ... 5",
    "Test 2 OK  6",
]
def get_log_from_disk(id):
    ## Your code comes here
    if id >= len(log_file):
        return None
    return log_file[id]

def get_log(request):
    log_id = 0
    if "log_id" in request.session:
        log_id = int(request.session['log_id'])
    results = get_log_from_disk(log_id)
    if results is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    request.session['log_id'] = int(log_id + 1)
    return HttpResponse(results)

def results(request):
    ## Your code comes here
    return render(request, 'results.html', {})

def submit(request):

    if request.method == 'POST':
        source_code = request.POST['source_code']
        # Process the source_code
        request.session['log_id'] = int(0)
        return HttpResponseRedirect(reverse('myapp.views.results'))

    return render(request, 'index.html', {'': ""})
