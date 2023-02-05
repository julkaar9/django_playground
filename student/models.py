from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    SEMESTER_CHOICES = ((1, "I"), (2, "II"), (3, "III"))

    roll = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    department = models.ForeignKey(
        Department, related_name="students", on_delete=models.CASCADE
    )
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES, default=1)

    def __str__(self):
        return f"{self.name} - {self.semester}"
