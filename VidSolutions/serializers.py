from rest_framework import serializers

from .models import user,VideoSolutions, Class



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ["first_name", "last_name", "address", "pincode"]


class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields = ["class_section"]

class VideoSolutionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = VideoSolutions
		fields = ["title", "class_section", "video"]
