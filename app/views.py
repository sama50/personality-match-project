from django.shortcuts import render , redirect
from app.models import Question , Options, MyUser, QueationAnswer
import uuid
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        crushname = request.POST.get('crushname')
        unique = uuid.uuid4()
        print(email)
        myuser = MyUser(email=email,name=name,crush=crushname,count=1,myid=unique)
        myuser.save()
        return redirect(f'/queations/{unique}/{Question.objects.all().first().id}/')
        # save here

    return render(request,'index.html')

def saveQueations(request,uuid,id): 
    if request.method == 'POST': 
        # save queation here 
        if id==1:
            id = Question.objects.all().first().id
        selected_option = request.POST.get('option')
        # print(selected_option)
        user = MyUser.objects.get(myid=uuid)
        name = user.name
        savequeationans = QueationAnswer(user=user,name=name,ans=selected_option)
        savequeationans.save()
        id = int(id)+1
        return redirect(f'/queations/{uuid}/{id}/')
    if Question.objects.all().count()<int(id):
            msg = "hey, Your Test Submit Successfuly and above link share your friend to find the personality meatch , and result get you on your mail"
            link = f'http://127.0.0.1:8000/share/{uuid}/{1}/'
            return render(request,'result.html',{'msg':msg,'link':link})
    id = Question.objects.all().first().id
    question = Question.objects.get(id=id)
    return render(request,'queations.html',{'question':question})

def otherpersontest(request,uuid,id):
    if request.method == 'POST':
        if id==1:
            id = Question.objects.all().first().id
        selected_option = request.POST.get('option') 
        user = MyUser.objects.get(myid=uuid)
        name = user.crush
        savequeationans = QueationAnswer(user=user,name=name,ans=selected_option)
        savequeationans.save()
        id = int(id)+1
        return redirect(f'/share/{uuid}/{id}/')
    if Question.objects.all().count()<int(id):
            # calculate the score of user and crush 
            user = MyUser.objects.get(myid=uuid) 
            userans = QueationAnswer.objects.filter(user=user,name=user.name)
            otherperosnans = QueationAnswer.objects.filter(user=user,name=user.crush)
            commanans = 0 
            for i in range(0,len(userans)):
                fuans = userans[i].ans
                ouans = otherperosnans[i].ans
                if fuans == ouans: 
                    commanans = commanans+1 
            print(commanans)
            send_mail(f'Personality match, your personality match result with your friend',f'here it result {commanans*(Question.objects.all().count())}/100,\nit totaly depend on the how they answer the queations.\nall queation is the best queation to test personality meatch',settings.EMAIL_HOST_USER,[user.email])
            return render(request,'result.html',{'msg':'Done...'})
    id = Question.objects.all().first().id
    question = Question.objects.get(id=id)
    return render(request,'queations.html',{'question':question})