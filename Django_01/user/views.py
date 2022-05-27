from django.shortcuts import render, redirect

# user/views.py
def sign_up_view(request):
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        return render(request, 'user/index.html')
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우

        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if password != password2:
            return render(request, 'user/index.html')
        else:
            new_user = UserModel()
            new_user.email = email
            new_user.password = password
            new_user.save()
        return redirect('/sign-in')