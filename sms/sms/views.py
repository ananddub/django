from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from database.models import Student

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(roll=username,password=password)
            return render(request, 'profile.html', {'student': student})
        except Student.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid roll number.'})
    else:
        return render(request, 'login.html')



def forgot_password(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password != repassword:
            return render(request, 'forgot_password.html', {'error_message': 'Passwords do not match'})
        try:
            student = Student.objects.get(roll=roll)
        except Student.DoesNotExist:
            return render(request, 'forgot_password.html', {'error_message': 'Invalid roll number.'})
        student.password =password 
        student.save()
        return redirect('login')

    return render(request, 'forgot_password.html')


