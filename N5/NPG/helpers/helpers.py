from django.http import HttpResponseBadRequest

def ajax_required(f):  
    def wrap(request, *args, **kwargs):

        print(request)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            return f(request, *args, **kwargs)
        return HttpResponseBadRequest()
                
    return wrap
