from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from mainpage.forms import ApplyForm
from mainpage.models import Comment, Direction, Socials, Advantage, Course, Speaker, Manager, Director, Application


# Create your views here.


def main(request):
    comments = Comment.objects.all()
    directions = Direction.objects.all()
    socials = Socials.objects.all()
    advantages = Advantage.objects.all()
    courses = Course.objects.all()
    return render(request,
                  'main.html',
                  {
                      'comments': comments,
                      'directions': directions,
                      'socials': socials,
                      'advantages': advantages,
                      'courses': courses,
                      'status': 'main',
                      'form': ApplyForm(),
                  }
                  )


def get_course(request, course_id):
    socials = Socials.objects.all()
    course = Course.objects.get(id=course_id)
    teachers = set()
    for m in course.modules.all():
        teachers.add(m.speaker)
    return render(request,
                  'current_school.html',
                  {
                      'socials': socials,
                      'course': course,
                      'teachers': teachers,
                      'modules': course.modules.all(),
                      'intentions': course.intention_set.all(),
                      'status': 'courses',
                      'form': ApplyForm(),
                  }
                  )


def all_courses(request):
    directions = Direction.objects.all()
    courses = Course.objects.all()
    return render(request,
                  'courses.html',
                  {
                      'directions': directions,
                      'courses': courses,
                      'status': 'courses',
                  }
                  )


def all_comments(request):
    page = request.GET.get('page', 1)
    comments = Comment.objects.all()
    paginator = Paginator(comments, 2)
    result = paginator.get_page(page)
    max_page = paginator.num_pages
    return render(request, 'reviews.html',
                  {
                      'comments': result,
                      'page': int(page),
                      'max_page': int(max_page),
                      'paginator': paginator,
                      'page_range': range(1, max_page+1),
                      'status': 'reviews',
                  })


def contacts(request):
    managers = Manager.objects.all()
    directors = Director.objects.all()
    return render(request, 'contacts.html',
                  {
                      'managers': managers,
                      'directors': directors,
                      'status': 'contacts',
                  })


def apply(request):
    form = ApplyForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        app = Application()
        app.name = data['name']
        app.phone = data['phone']
        app.course = data['program']
        app.save()
    return HttpResponseRedirect('/')