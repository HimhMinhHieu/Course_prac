from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, generics

from .models import Category, Course

# Create your views here.
from .paginator import CourseSetPagination
from .serializers import CategorySerializer, CourseSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CourseSetPagination

class CategoryView(View):

    def get(self, request):
        cats = Category.objects.all()
        return render(request, 'courses/list.html', {
            'categories': cats
        })

    def post(self, request):
        pass

def index(request):
    return HttpResponse('HELLO CS2001')

def list(request, course_id):
    return HttpResponse(f'COURSE {course_id}')
