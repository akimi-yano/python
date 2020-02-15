from django.db import models

class CourseManager(models.Manager):
    def validator(self, post_data):
        errors={}
        if len(post_data['name'])<=5:
            errors['name']="Name must be more than 5 characters"

        if len(post_data['description'])<=15:
            errors['description']="Description must be more than 15 characters"

        return errors


class Course(models.Model):
    name=models.CharField(max_length=45)
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = CourseManager()
    