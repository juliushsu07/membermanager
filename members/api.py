from members.models import Member
from rest_framework import viewsets, permissions
from .serializers import MemberSeriralizer

# Lead Viewset
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = MemberSeriralizer