from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel
from .serializers import MyModelSerializer
from django.core import serializers
from django.http import HttpResponse

@csrf_exempt
def serial_list(request):
    if request.method == 'GET':
        snippets = MyModel.objects.all()
        serializer = MyModelSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = MyModelSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def serial_detail(request, pk):
    try:
        snippet = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MyModelSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = serializers.deserialize("json", request.body)
        serializer = MyModelSerializer(data.object, data=data.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
