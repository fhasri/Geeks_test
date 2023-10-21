

from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers



@api_view(['GET'])
def task_list(request):
    queryset = Task.objects.all()
    serializer = serializers.TaskSerializer(queryset, many = True) 
    return Response(serializer.data, status=200) 

@api_view(['GET'])
def task_detail(request, pk):
    try:
        queryset = Task.objects.get(id = pk)
        serializer = serializers.TaskSerializer(queryset)
        return Response(serializer.data, status=200)
    except Task.DoesNotExist:
    
        return Response( f'status did not found {pk}!', status=404)
    
@api_view(['POST'])
def task_create(request):
    # print(request.data, '!!!!!!!!!!!!!')
    serializer = serializers.TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data , status=201 )


@api_view(['DELETE'])
def task_delate(request, pk):
    # serializer = serializers.Task()
    try:
        task = Task.objects.get(id = pk)
        task.delete()
        return Response ('Deleted Seccesfully', status=204)
    except Task.DoesNotExist:
        return Response(f'Task with key {pk} Deteled. Task Does not exist', status=404 )
    

@api_view(['PUT', 'PATCH'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.TaskSerializer(instance=task, data=request.data)
        else:
            serializer = serializers.TaskSerializer(instance=task, data=request.data, partial =True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=206) 
    except Task.DoesNotExist:
        return Response('Does not exist', status=404)
    
    