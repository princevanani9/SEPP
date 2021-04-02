from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from candidate.forms import CandidateForm
from candidate.models import Candidate
from django.contrib.auth.models import User
from users.models import UserProfile



from django.contrib.auth.decorators import login_required



def home(request):    
    return render(request,'election/home.html')

@login_required
def candidate(request):
    if request.user.is_staff == True:
        return HttpResponseRedirect('/NotAllow/')
    if request.method == "POST":
        f=CandidateForm(request.POST)
        if Candidate.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('/Present/')
        if f.is_valid():
            name=f.cleaned_data['name']
            description=f.cleaned_data['Description']
            image=f.cleaned_data['image']
            election_type=f.cleaned_data['election_type']
            can=Candidate(user=request.user,name=name,Description=description,image=image,election_type=election_type)
            can.save()
            return HttpResponseRedirect('/')
    else:
        f=CandidateForm()
    return render(request,'candidate/candidate.html',{'form':f})

@login_required
def vote(request):
    if request.user.is_staff == True:
        return HttpResponseRedirect('/NotAllow/')
    context = []
    pos = Candidate.objects.all()
    user = User.objects.get(username=request.user.username)
    profile = UserProfile.objects.get(user=user)
    if profile.voted == True:
        return HttpResponseRedirect('/Voted/')
    for c in pos:
       context.append([c,c.image.url])
    if request.method == 'POST':
        selected_candidate = Candidate.objects.get(name=request.POST['candidate'])
        selected_candidate.votes += 1
        selected_candidate.save()
        profile.voted = True
        profile.save()
        return HttpResponseRedirect('/')
    return render(request, 'election/vote.html', {'candidates':context})


def about(request):
    return render(request,'election/about.html', {'title': 'About'})

@login_required
def voted(request):
    return render(request,'election/voted.html')

@login_required
def notallow(request):
    return render(request,'election/notallow.html')

@login_required
def result(request):
    pos=Candidate.objects.all()
    context = []
    for c in pos:
       context.append([c,c.image.url])
    return render(request,'election/result.html',{'pos':context})

@login_required
def presentcandidate(request):
    return render(request,'election/present.html')



