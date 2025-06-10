from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Quiz,EmailOtp,score
from django.core.paginator import Paginator
import random
from .utils import send_otp_mail
# Create your views here.
User = get_user_model()

@login_required(login_url='login')
def result(request):
    request.session['result_page']='yes'
    page_number = request.session.get('page_number')
    total_pages = request.session.get('total_pages')
    category = request.session.get('category')
    difficulty = request.session.get('difficulty')
    session_score = request.session.get('score')
    if page_number is None:
        messages.error(request,'First play the quiz to see the result')
        return redirect('category')
    if page_number <= total_pages:
        return redirect('home')
    user_score = score.objects.filter(user=request.user,category=category,difficulty=difficulty).first()
    if user_score:
        if user_score.score < session_score:
            user_score.score = session_score
            user_score.save()
    else:
        score.objects.create(user=request.user, category=category, difficulty=difficulty, score=session_score)
    return render(request,'result.html')

@login_required(login_url='login')
def category(request):
    if request.session.get('result_page') == 'yes':
        return redirect('result')
    request.session.pop('page_number', None)
    request.session.pop('result_page', None)
    request.session.pop('category', None)
    request.session.pop('difficulty', None)
    request.session.pop('random_quiz', None)
    request.session.pop('total_pages', None)
    request.session.pop('answer', None)
    request.session.pop('selected_option', None)
    request.session['score']=0
    request.session['all_answers'] = []
    if request.method == "POST":
        category = request.POST.get('category')
        level = request.POST.get('level')
        if category is None:
            messages.error(request,'Please select categroy')
            return redirect('category')
        elif level is None:
            messages.error(request,'Please select difficulty level')
            return redirect('category')
        else:
            if Quiz.objects.filter(category=category,difficulty=level).exists():
                quizgame = Quiz.objects.filter(category=category,difficulty=level)
            else:
                messages.error(request,'No quiz available for this category and difficulty level')
                return redirect('category')
            random_quiz = random.sample(list(quizgame), min(10, quizgame.count()))
            random_quiz_ids = [quiz.id for quiz in random_quiz]
            request.session['random_quiz'] = random_quiz_ids
            return redirect('home')
            
    return render(request,'category.html')

@login_required(login_url='login')
def home(request):
    if request.session.get('result_page') == 'yes':
        return redirect('result')
    request.session.pop('result_page',None)
    quizgame_id = request.session.get('random_quiz')
    if quizgame_id is None:
        messages.error(request,'Please select category and difficulty level')
        return redirect('category')
    quizgame = Quiz.objects.filter(id__in = quizgame_id)
    paginator = Paginator(quizgame,1)
    page_number = request.session.get('page_number') 
    if page_number is None:
        page_number = 1
    request.session['page_number'] = page_number
    quizes = paginator.get_page(page_number)
    quiz = quizes[0]
    options = [quiz.option1,quiz.option2,quiz.option3,quiz.option4]
    request.session['total_pages'] = paginator.num_pages
    request.session['category'] = quiz.category
    request.session['difficulty'] = quiz.difficulty
    context={
        'quizgame':quizes,
        'current_page': int(page_number),
        'value': int(page_number)*10,
        'options': options,
        'category': quiz.category,
        'difficulty': quiz.difficulty,
    } 
    return render(request, 'home.html', context)

def logout(request):
    auth.logout(request)
    return redirect('login')

def quit(request):
    request.session.pop('page_number', None)
    request.session.pop('answer', None)
    request.session.pop('selected_option', None)
    request.session.pop('score', None)
    request.session.pop('random_quiz', None)
    request.session.pop('total_pages', None)
    request.session.pop('all_answers', None)
    messages.success(request,'You have successfully quit the quiz')
    return redirect('category')

def checkans(request,id):
    if request.method == "POST":
        selected_option = request.POST.get('selected_options')
        if selected_option == "Next":
            request.session['page_number'] = int(request.GET.get('page'))+1
            request.session.pop('answer', None)
            request.session.pop('selected_option', None)
            if request.session['page_number'] > request.session['total_pages']:
                return redirect('result')
            return redirect('home')
        else:
            request.session['page_number'] = int(request.GET.get('page')) 
        request.session['all_answers'] += [selected_option]  
        question1 = get_object_or_404(Quiz, id=id)
        if question1.answer == selected_option:
            request.session['selected_option'] = selected_option
            request.session['answer'] = 'correct'
            request.session['score'] += 1
            return redirect('home')
        else:
            request.session['selected_option'] = selected_option
            request.session['answer'] = 'incorrect'
            return redirect('home')

def login(request):
    request.session.pop('result_page', None)
    request.session.pop('page_number', None)
    request.session.pop('random_quiz', None)
    request.session.pop('total_pages', None)
    request.session.pop('answer', None)
    request.session.pop('selected_option', None)
    request.session.pop('score', None)
    request.session.pop('all_answers', None)
    request.session.pop('category', None)
    request.session.pop('difficulty', None)
    if request.user.is_authenticated:
        return redirect('quiz_home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('quiz_home')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already taken')
            return redirect('register')
        if password1 != password2:
            messages.error(request,'Password does not match')
            return redirect('register')
        request.session['temp_user']={'email':email}
        send_otp_mail(email)
        User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        messages.success(request,'User created successfully')
        return redirect('login')
    return render(request,'register.html')
    
def remove_result(request):
    request.session.pop('result_page',None)
    return redirect('category')

def quiz_home(request):
    return render(request,'quiz_home.html')

def answer(request):
    all_answers = request.session.get('all_answers')
    if len(all_answers) < 10:
        messages.error(request,'Please play the quiz to view the answers')
        return redirect('category')
    quizgame_id = request.session.get('random_quiz')
    if quizgame_id is None:
        messages.error(request,'Please play the quiz to view the answers')
        return redirect('category')
    quizgame = Quiz.objects.filter(id__in = quizgame_id)
    quiz = quizgame[0]
    
    quiz_and_answers = zip(quizgame, all_answers)
    context={
        'category': quiz.category,
        'difficulty': quiz.difficulty,
        'quiz_and_answers': quiz_and_answers,
    }
    return render(request,'answer.html',context)

def record(request):
    user_scores = score.objects.filter(user=request.user)
    total_score = user_scores[0].score
    return render(request,'record.html',{'score':total_score})