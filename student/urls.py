from django.urls import path
from .views import (
    DepartmentListView,
    StudentListView,
    StudentView,
    StudentAggregateView,
    TotalProductSales,
)

app_name = "student"

urlpatterns = [
    path("department/", DepartmentListView.as_view(), name="department"),
    path("student/v1/", StudentListView.as_view(), name="student_listv1"),
    path(
        "student/aggregate/", StudentAggregateView.as_view(), name="student_aggregate"
    ),
    path("student/v1/<int:pk>", StudentView.as_view(), name="studentv1"), 
]
