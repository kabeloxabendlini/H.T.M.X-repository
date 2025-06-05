"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
def edit_student(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {}
    context['student'] = student
    context['form'] = StudentForm(initial={
        'first_name':student.first_name,
        'last_name': student.last_name,
        'gender': student.gender,
        'age': student.age,
        'major': student.major
    })
    return render(request, 'partial/student/edit_student.html', context)

def edit_student_submit(request, student_pk):
    context = {}
    student = Student.objects.get(pk=student_pk)
    context['student'] = student
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'partial/student/edit_student.html', context)
    return render(request, 'partial/student/student_row.html', context)