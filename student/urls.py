from django.urls import path
from .views import (
    DepartmentListView,
    StudentListView,
    StudentView,
    StudentAggregateView,
)

app_name = "student"

# The necessary views are imported and connected to their respective urls
urlpatterns = [
    path("department/", DepartmentListView.as_view(), name="department"),
    path("student/v1/", StudentListView.as_view(), name="student_listv1"),
    path(
        "student/aggregate/", StudentAggregateView.as_view(), name="student_aggregate"
    ),
    # <int:pk> here pk is used as a variable, the value is then passed to the view
    path("student/v1/<int:pk>", StudentView.as_view(), name="studentv1"),
]
