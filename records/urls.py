from django.urls import path
from records.views import *

urlpatterns = [

 path('dashboard/', dashboard, name='dashboard'),
 path('python/', python, name='python'),
 path('java/', java, name='java'),
 path('java-script/', javascript, name='javascript'),
 path('django/', django, name='django'),
 path('machine-learning/', machine_learning, name='machinelearning'),
 path('linux/', linux, name='linux'),
 path('python/<int:blog_id>/', blog_python, name='blog_python'),
 path('linux/<int:blog_id>/', blog_linux, name='blog_linux'),
 path('java/<int:blog_id>/', blog_java, name='blog_java'),
 path('java-script/<int:blog_id>/', blog_js, name='blog_js'),
 path('machine-learning/<int:blog_id>/', blog_ml, name='blog_ml'),
 path('django/<int:blog_id>/', blog_django, name='blog_django')

 # path('add-blog/', AddBlog.as_view(), name="addBlog")
]
