from rest_framework import serializers

from .models import Department, Student


class DepartmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Department
        read_only_fields = (
            "id",
            "name",
        )
        fields = read_only_fields


class StudentSerializer(serializers.ModelSerializer):
    # department = DepartmentSerilaizer()

    class Meta:
        model = Student
        read_only_fields = ("id",)
        fields = ("id", "roll", "name", "department", "semester")
