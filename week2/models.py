from django.db import models

# 1. ONE-TO-MANY (ForeignKey)
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Relationship

    def __str__(self):
        return self.title


# 2. ONE-TO-ONE
class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)

    # One-to-One relationship
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_name


# 3. MANY-TO-MANY
class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title
