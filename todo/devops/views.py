from django.http import JsonResponse, HttpResponse

def health_check(request):
    return JsonResponse({'status': 'ok'})