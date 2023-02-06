from datetime import datetime
from django.db import models

# Create your models here.


class Department(models.Model):
    """Creates a department table with the following fields

    name: varchar / charfield, name of department
    created_at: Datetime field

    """

    name = models.CharField(max_length=128)
    created_at = models.DateTimeField("Entry Date", default=datetime.now)

    def __str__(self):
        """Overriding the string representation, useful for debugging or admin display"""
        return self.name


class Student(models.Model):
    """Creates a student table with the following fields

    semester_choices are used as for semester's choicefield

    roll: varchar / charfield, unique roll number
    name: varchar / charfield, name of student
    department: Foreign Key to department table, cascades on deletion
    semester: ChoiceField, semester of each student, can only accept 3 values, [1, 2 and 3]
    created_at: Datetime field

    """

    SEMESTER_CHOICES = ((1, "I"), (2, "II"), (3, "III"))

    roll = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    department = models.ForeignKey(
        Department, related_name="students", on_delete=models.CASCADE
    )
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES, default=1)
    created_at = models.DateTimeField("Entry Date", default=datetime.now)

    def __str__(self):
        return f"{self.name} - {self.semester}"
