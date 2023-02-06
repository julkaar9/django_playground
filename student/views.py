from django.http import Http404
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Student, Department
from .serializers import StudentSerializer, DepartmentSerilaizer


class DepartmentListView(APIView):
    """
    This view is used to list all available instances of department data
    """

    def get(self, request):
        """
        This module responds to http GET requests, similarily use post, put, etc
        for their respective HTTP methods
        """
        # .objects  is used to perform data base operations, such as retrieving, etc
        # here we are retrieving all the instances of department using objects.all()
        query = Department.objects.all()
        print(query)
        # Here we serialize the retrieved data instances, many=True means there are
        # multuple instances
        serializer = DepartmentSerilaizer(query, many=True)
        print(serializer.data)
        # Here the json is send as response to the client
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self, request):
        query = Student.objects.all()
        print(query)
        serializer = StudentSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Here we are performing a deserialization, where the request json data
        # is being converted into model instance
        serializer = StudentSerializer(data=request.data)
        # Checks whether the given data is valid other-wise raises error
        if serializer.is_valid():
            # Saves the data in the database of is_valid is true
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    def get_obj(self, pk):
        """Helper function to fetch student instance using pk"""
        try:
            query = Student.objects.get(id=pk)
            return query
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_obj(pk)
        serializer = StudentSerializer(query)
        return Response(serializer.data)

    def put(self, request, pk):
        """Similar to POST, but we update the current data with the received data"""
        query = self.get_obj(pk)
        serializer = StudentSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        query = self.get_obj(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAggregateView(APIView):
    """View to perform aggregation"""

    def get(self, request):
        # Grab the group_by and value url parms

        group_by = request.GET.get("group_by")
        value = request.GET.get("value")

        if group_by is None and value is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # if both group_by and value is None, return all the instances
        if group_by is None:
            query = Student.objects.all()
        else:
            # This orm operation performs the group_by
            query = Student.objects.values(group_by).annotate(count=Count(group_by))
            if value is not None:
                query = Student.objects.filter(**{group_by: value}).count()
        print(query)
        return Response(query)
