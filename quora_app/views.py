from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like, CustomUser


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page or wherever you want
        else:
            messages.error(request, 'Username is already taken.')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('view_questions')  # Replace 'home' with your homepage URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_question(request):
    if request.method == 'POST':
        text = request.POST['text']
        Question.objects.create(user=request.user, text=text)
    return redirect('view_questions')

@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        text = request.POST['text']
        question = Question.objects.get(pk=question_id)
        Answer.objects.create(user=request.user, question=question, text=text)
    return redirect('view_questions')

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    Like.objects.create(user=request.user, answer=answer)
    return redirect('view_questions')

def view_questions(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    likes_dict={}
    for i in answers:
        likes = Like.objects.filter(answer=i).count()
        likes_dict[i.id]=likes
    print(likes_dict,".........")
    return render(request, 'questions.html', {'questions': questions, 'answers': answers, 'likes': likes_dict})
