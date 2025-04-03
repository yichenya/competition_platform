from rest_framework import serializers
from .models import Registration, School,Competition

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name']


class RegistrationSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)  # 只读字段，显示学校名称

    class Meta:
        model = Registration
        fields = ['id', 'name', 'student_id', 'school', 'school_name', 'teacher_name', 'teacher_phone', 'created_at']


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'registration_deadline']
