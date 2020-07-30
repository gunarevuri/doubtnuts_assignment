from django.shortcuts import render, HttpResponse

from .models import user,VideoSolutions,Class

from .serializers import UserSerializer, VideoSolutionsSerializer, ClassSerializer

from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

def index(request):
	return HttpResponse('<h3>Hi all</h3>')


@api_view(['GET'])
def users_list(request):
	if request.method == 'GET':
		users = user.objects.all()
		serialzer = UserSerializer(users, many = True)
		return Response(serialzer.data)


@api_view(['GET'])
def get_all_videos(request):
	if request.method == 'GET':
		videos = VideoSolutions.objects.all()
		serializer = VideoSolutionsSerializer(videos, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def get_class_videos(request, id):
	if request.method == 'GET':
		videos = VideoSolutions.objects.all()
		l = []
		serializer = VideoSolutionsSerializer(videos, many=True)
		for obj in serializer.data:
			if obj["class_section"] == id:
				l.append(obj)
		return Response(l)

@api_view(["GET"])
def get_all_classes(request):
	if request.method == 'GET':
		all_classes = Class.objects.all()
		serializer = ClassSerializer(all_classes, many = True)
		return Response(serializer.data)





