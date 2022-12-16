from rest_framework import serializers 
from members.models import Member


# Member Serializer
class MemberSeriralizer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'