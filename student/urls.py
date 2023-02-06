from django.urls import path
from .views import (
    DepartmentListView,
    StudentListView,
    StudentView,
    StudentAggregateView,
    StudentReport,GroupByIntro
)

app_name = "student"

urlpatterns = [
    path("department/", DepartmentListView.as_view(), name="department"),
    path("student/v1/", StudentListView.as_view(), name="student_listv1"),
    path(
        "student/aggregate/", StudentAggregateView.as_view(), name="student_aggregate"
    ),
    path("student/v1/<int:pk>", StudentView.as_view(), name="studentv1"),
    path("student/dashboard/", GroupByIntro.as_view(), name="dashboard"),
]
