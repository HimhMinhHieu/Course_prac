from rest_framework.serializers import ModelSerializer

from courses.models import Category

from courses.models import Course


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date', 'updated_date']

class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        # fields = ['id', 'subject', 'created_date', 'category']
        exclude = ('tags',)