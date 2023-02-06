from django.http import Http404
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Student, Department
from .serializers import StudentSerializer, DepartmentSerilaizer

from django.db.models import Sum
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField


class DepartmentListView(APIView):
    def get(self, request):
        query = Department.objects.all()
        print(query)
        serializer = DepartmentSerilaizer(query, many=True)
        print(serializer.data)
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self, request):
        query = Student.objects.all()
        print(query)
        serializer = StudentSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    def get_obj(self, pk):
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
    def get(self, request):
        group_by = request.GET.get("group_by")
        value = request.GET.get("value")
        if group_by is None and value is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        print(group_by)
        if group_by is None:
            query = Student.objects.all()
        else:
            query = Student.objects.values(group_by).annotate(count=Count(group_by))
            if value is not None:
                query = Student.objects.filter(**{group_by: value}).count()
        print(query)
        return Response(query)


class StudentReport(SlickReportView):
    report_model = Student

    date_field = "created_at"
    # a date/datetime field on the report model

    # fields on the report model ... surprise !
    columns = ["roll", "name", "department", "semester"]


class GroupByIntro(SlickReportView):

    report_model = Student
    date_field = "created_at"

    group_by = "semester"
    # We can group_by a foreign key or date field

    columns = [
        "name",
        SlickReportField.create(
            method=Count,
            field="roll",
            name="roll__sum",
            verbose_name=("Total Students $"),
        )
        # a Slick Report Field is responsible for carrying on the needed calculation(s).
    ]
    chart_settings = [
        {
            "type": "bar",
            "data_source": [
                "roll__sum"
            ],  # the name of the field containing the data values
            "title_source": ["name"],  # name of the field containing the data labels
            "title": "Pie Chart (Quantities) Highcharts",  # to be displayed on the chart
        }
    ]
