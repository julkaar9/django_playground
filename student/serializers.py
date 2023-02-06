from rest_framework import serializers

from .models import Department, Student


class DepartmentSerilaizer(serializers.ModelSerializer):
    """ Serializer for Deparment model """
    class Meta:
        """ The meta nested class is used to specify model specific information
        
        model: The django model to be serializer / or deserialized
        read_only_field: Model fields that are auto created or cannot be updated,
                         generally, primary_key or login time, etc.
        
        fields: Model fields user serialization / or deserialization
        """
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
