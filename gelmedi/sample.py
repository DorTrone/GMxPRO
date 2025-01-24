from django.db import models

class Fakultet(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class Kafedra(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Group(models.Model):
    short_name = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.course.name})"

class Student(models.Model):
    STATUS_CHOICES = [
        ('present', 'geldi'),
        ('late', 'gija galdy'),
        ('reason absent', 'sebapli gelmedi'),
        ('no reason absent', 'sebapsiz gelmedi')
    ]

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    par_phone = models.CharField(max_length=15, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='present')

    def __str__(self):
        return f"{self.full_name} {self.group.short_name} ({self.get_status_display()})"
