from entities.models import User, Group
from entities.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets

class DynamicDepthViewSet(viewsets.ModelViewSet):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = 0
        try:
            depth = int(self.request.query_params.get('depth', 0))
        except ValueError:
            pass # Ignore non-numeric parameters and keep default 0 depth
        
        context['depth'] = depth

        return context

class UserViewSet(DynamicDepthViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(DynamicDepthViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer