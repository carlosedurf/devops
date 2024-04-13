from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = {'tasks': list(tasks.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title', ''),
            description=data.get('description', ''),
            completed=data.get('completed', False)
        )
        return JsonResponse({'id': task.id}, status=201)

@csrf_exempt
def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'GET':
        data = {
            'title': task.title,
            'description': task.description,
            'completed': task.completed
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        task.save()
        return JsonResponse({'message': 'Task updated successfully'})

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)
