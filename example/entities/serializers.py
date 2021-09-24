from entities.models import User, Group
from rest_framework import serializers

class DynamicDepthSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get('depth', 0)

class UserSerializer(DynamicDepthSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'mail']

class GroupSerializer(DynamicDepthSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'members']