from django.shortcuts import render
from records.models import *
from django.views.generic import View
from records.forms import BlogDetailsForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def dashboard(request):
    details = Details.objects.filter(id=1).values('about','email', 'contact')

    context = {
        'details': details
    }
    return render(request, 'index.html', context)


def python(request):
    blog_details_python = BlogDetails.objects.filter(technology=1).values('id', 'technology', 'short_details',
                                                                          'description',
                                                                          'blog_details_photo',
                                                                          'written_by')
    details = Details.objects.filter(id=1).values('about', 'email', 'contact')

    blog_detail = BlogDetails.objects.filter(technology=1, pk=1).values('technology', 'short_details', 'description',
                                                                        'blog_details_photo',
                                                                        'written_by')

    return render(request, 'python.html',
                  {'blog_details_python': blog_details_python, 'bbb': blog_detail, 'details': details})


def blog_python(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=1, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about', 'email', 'contact')

    return render(request, 'blog_python.html', {'blog_details': blog_detail, 'details': details})


def java(request):
    blog_details_java = BlogDetails.objects.filter(technology=6).values('technology', 'short_details', 'description',
                                                                        'blog_details_photo',
                                                                        'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'Java.html', {'blog_details_java': blog_details_java, 'details': details})


def blog_java(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=6, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'blog_java.html', {'blog_details': blog_detail, 'details': details})


def django(request):
    blog_details_django = BlogDetails.objects.filter(technology=5).values('technology', 'short_details', 'description',
                                                                          'blog_details_photo',
                                                                          'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'Django.html', {'blog_details_django': blog_details_django, 'details': details})


def blog_django(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=5, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'blog_django.html', {'blog_details': blog_detail, 'details': details})


def javascript(request):
    blog_details_javascript = BlogDetails.objects.filter(technology=3).values('technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about', 'email', 'contact')

    return render(request, 'JavaScript.html', {'blog_details_javascript': blog_details_javascript, 'details': details})


def blog_js(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=3, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'blog_js.html', {'blog_details': blog_detail, 'details': details})


def machine_learning(request):
    blog_details_ml = BlogDetails.objects.filter(technology=7).values('technology', 'short_details', 'description',
                                                                      'blog_details_photo',
                                                                      'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'MachineLearning.html', {'blog_details_ml': blog_details_ml, 'details': details})


def blog_ml(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=7, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'blog_ml.html', {'blog_details': blog_detail, 'details': details})


def linux(request):
    blog_details_linux = BlogDetails.objects.filter(technology=4).values('technology', 'short_details', 'description',
                                                                         'blog_details_photo',
                                                                         'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'linux.html', {'blog_details_linux': blog_details_linux, 'details': details})


def blog_linux(request, blog_id):
    blog_detail = BlogDetails.objects.filter(technology=4, pk=blog_id).values('id', 'technology', 'short_details',
                                                                              'description',
                                                                              'blog_details_photo',
                                                                              'written_by')
    details = Details.objects.filter(id=1).values('about','email',  'contact')

    return render(request, 'blog_linux.html', {'blog_details': blog_detail, 'details': details})

#
# class AddBlog(View):
#
#     def get(self, request):
#         form = BlogDetailsForm()
#         return render(request, 'addBlog.html', {"form": form})
#
#     def post(self, request):
#         form = BlogDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect(reverse('records:dashboard'))


