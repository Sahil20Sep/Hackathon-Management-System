from django.shortcuts import render
from Hackathon_Management_System.models import ParticipantModel
from Hackathon_Management_System.models import HackathonModel
from django.contrib import messages
from Hackathon_Management_System.forms import Participantforms, Hackathonforms
from django.db import connection

def HomePage(request):
    return render(request,'main.html')

def showpart(request):
    showall=ParticipantModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def showhack(request):
    showall=HackathonModel.objects.all()
    return render(request,'Index2.html',{"data":showall})

def Insertpart(request):
    if request.method=="POST":
        if request.POST.get('part_id') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email_add') and request.POST.get('dob') and request.POST.get('student') and request.POST.get('college') and request.POST.get('cpi'):
            saverecord=ParticipantModel()
            saverecord.part_id=request.POST.get('part_id')
            saverecord.first_name=request.POST.get('first_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.email_add=request.POST.get('email_add')
            saverecord.dob=request.POST.get('dob')
            saverecord.student=request.POST.get('student')
            saverecord.college=request.POST.get('college')
            saverecord.cpi=request.POST.get('cpi')
            saverecord.save()
            messages.success(request,'Participant '+saverecord.part_id+ ' is Saved Successfully..!')
            return render(request,'Insert.html')
    else:
        return render(request,'Insert.html')

def Inserthack(request):
    if request.method=="POST":
        if request.POST.get('hack_id') and request.POST.get('hack_name') and request.POST.get('name_type') and request.POST.get('date') and request.POST.get('time') and request.POST.get('duration'):
            saverecord=HackathonModel()
            saverecord.hack_id=request.POST.get('hack_id')
            saverecord.hack_name=request.POST.get('hack_name')
            saverecord.name_type=request.POST.get('name_type')
            saverecord.date=request.POST.get('date')
            saverecord.time=request.POST.get('time')
            saverecord.duration=request.POST.get('duration')
            saverecord.save()
            messages.success(request,'Hackathon '+saverecord.hack_id+ ' is Saved Successfully..!')
            return render(request,'Insert2.html')
    else:
        return render(request,'Insert2.html')

def Editpart(request,id):
    editpartobj=ParticipantModel.objects.get(part_id=id)
    return render(request,'Edit.html',{"ParticipantModel":editpartobj})

def updatepart(request,id):
    Updatepart=ParticipantModel.objects.get(part_id=id)
    form=Participantforms(request.POST,instance=Updatepart)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully..!')
        return render(request,'Edit.html',{"ParticipantModel":Updatepart})

def Edithack(request,id):
    edithackobj=HackathonModel.objects.get(hack_id=id)
    return render(request,'Edit2.html',{"HackathonModel":edithackobj})

def updatehack(request,id):
    Updatehack=HackathonModel.objects.get(hack_id=id)
    form=Hackathonforms(request.POST,instance=Updatehack)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully..!')
        return render(request,'Edit2.html',{"HackathonModel":Updatehack})

def Delpart(request,id):
    delpart=ParticipantModel.objects.get(part_id=id)
    delpart.delete()
    showdata=ParticipantModel.objects.all()
    return render(request,"Index.html",{"data":showdata})

def Delhack(request,id):
    delhack=HackathonModel.objects.get(hack_id=id)
    delhack.delete()
    showdata=HackathonModel.objects.all()
    return render(request,"Index2.html",{"data":showdata})

def sortParticipant(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=ParticipantModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'Sort.html',context)
    else:
        return render(request,'Sort.html')

def sortHackathon(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=HackathonModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'Sort2.html',context)
    else:
        return render(request,'Sort2.html')

def runQuerypart(request):
    raw_query = "select * from participant where first_name like 'S%' or last_name like '%s' order by part_id;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQuerypart.html',{'data':alldata})

