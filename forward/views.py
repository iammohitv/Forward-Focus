from django.shortcuts import render,redirect,get_object_or_404
#from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from .models import ProfileResult,Registration,ProfileEvaluation,Dummy, Gre_CSEECE,Gre_MechanicalCivil,Cat,GREScore,CATScore,Score1_Evaluation_GRE,Score2_Evaluation_GRE,Score3_Evaluation_GRE,Score4_Evaluation_GRE,Score_Result_GRE,Score_Result_GRE
from .forms import Form_profile,Form_profileresult
from django.contrib.auth.models import  auth, User
# Create your views here.

def quiz(request):
    return render(request,'quizpage.html')
#HOME PAGE
def add(request):

    return render(request,"main.html")
#REGISTRATION
def index(request):
    if request.method == 'POST':
        first_name = request.POST['field1']
        last_name = request.POST['field2']
        username = request.POST['field3']
        email = request.POST['field4']
        password1 = request.POST['field5']
        password2 = request.POST['field6']
        
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                 print('Username Taken')
                 messages.error(request,'Username already taken')
                 return redirect("/")
            elif User.objects.filter(email=email).exists():
                print('Email Already Exists')
                messages.error(request,'Email already exists')
                return redirect("/")
            else:   
              user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password1) 
              user.save();
              print('User Created')
              register = Registration(first_name=first_name,last_name=last_name,username=username, email=email, password1=password1, password2=password2)
              register.save();
              return redirect('login')
        
        else:
             print('Password Not Matching..')
             messages.error(request,'Password did not match')
             return redirect("/")
        #return redirect('login')   
    else:     

         return render(request,"index.html")
#LOGOUT

def logout(request):
             auth.logout(request)
             return redirect("/")


#LOGIN

def login(request):
    if request.method== 'POST':
                username= request.POST['username']
                password = request.POST[ 'password']

                user = auth.authenticate(username=username, password=password)
                if user is not None:
                        auth.login(request,user)
                        return redirect('home')
                else:
                         messages.error(request,'Invalid Credentials')   
                         print('Invalid Credentials')
                         return redirect('login')
    else:
                return render(request, 'loginn.html')


#PROFILE EVALUATION 

def evaluation(request):
    return render(request,'main_forms.html')


def Evalprofile(request):  
 
    current_user = request.user
    username_id = current_user.username
   # print(username_id)
    if ProfileEvaluation.objects.filter(username_id=username_id).exists():
    #    print(username_id)
        return redirect('updateprofile')
    else:    
        #return redirect('checkeval')
        return render(request,'main_forms.html')
            #form = EvalProfile()
            

         #else:     

#         return render(request,"main_forms.html")

def check_profile(request):

    #if request == 'POST':
        name= request.POST['field1']
        dob= request.POST['field2']
        contact= request.POST['field3']
        country= request.POST['field5']
        budget= request.POST['field6']
        degree= request.POST['field7']
        AOI_1= request.POST['field8']
        AOI_2= request.POST['field9']
        percentage_10= request.POST['field11']
        percentage_12= request.POST['field12']
        percentage_undergrad= request.POST['field13']
        backlogs= request.POST['field14']
        user_name = request.user
        username_id = user_name.username
    #profile is instance of table
        print(name)
        
        profile = ProfileEvaluation(name=name, dob=dob, contact=contact,  country=country,budget=budget,degree=degree,AOI_1=AOI_1,AOI_2=AOI_2,percentage_10=percentage_10,percentage_12=percentage_12,percentage_undergrad=percentage_undergrad,backlogs=backlogs,username_id = username_id)
        profile.save()
        return redirect('updateprofile')


            
    #return redirect('updateprofile')
    #return render(request,'main_forms.html')        

#PROFILE UPDATE


def UpdateProfile(request):

        current_user=request.user
        id=current_user.username
        instance = ProfileEvaluation.objects.get(username_id=id)
        form = Form_profile(instance=instance)
        if request.method == 'POST':
            form = Form_profile(request.POST or None,instance=instance)
            if form.is_valid():
                form.save()
                return redirect('updateprofile')
        context={
                     'instance':instance,
                     'form':form,
                        }
        return render(request,'update_profile.html',context)
        #return redirect('updateprofile')
    
def profile_result(request):
    current_user = request.user
    username_id = current_user.username
    if ProfileResult.objects.filter(username_id=username_id).exists():
        ProfileResult.objects.filter(username_id=username_id).delete() 
        profile = ProfileEvaluation.objects.get(username_id=username_id)
        country = profile.country
        degree = profile.degree
        if country == "India": 
            if degree == "MBA":
                exam_preffered= "CAT"
                print("CAT")
            elif degree == "MS":
                exam_preffered= "GATE"
                print("GATE")
            #context = {'exam_preffered':exam_preffered}
        elif country == "USA":
            if degree == "MS":
                exam_preffered= "GRE + TOEFL"
                print("GRE")
            elif degree == "MBA":
                exam_preffered= "GMAT + TOEFL/IELTS"
                print("GMAT")
        elif country == "Canada":
            if degree == "MS":
                exam_preffered = "GRE + IELTS"
            elif degree =="MBA":
                exam_preffered = "GMAT + IELTS"   
        else :
            if degree =="MS":
                exam_preffered = "GRE + IELTS/TOEFL"
            elif degree =="MBA":
                exam_preffered = "GMAT + IELTS/TOEFL"   
    
            
        profile_result = ProfileResult(exam_preffered=exam_preffered,username_id=username_id)
        profile_result.save()
        return render(request,'profile.html',{'exam_preffered':exam_preffered})

        
        
    else:
        profile = ProfileEvaluation.objects.get(username_id=username_id)
        country = profile.country
        degree = profile.degree
        if country == "India": 
                if degree == "MBA":
                    exam_preffered= "CAT"
                    print("CAT")
                elif degree == "MS":
                    exam_preffered= "GATE"
                    print("GATE")   
        elif country == "USA":
            if degree == "MS":
                exam_preffered= "GRE + TOEFL"
                print("GRE")
            elif degree == "MBA":
                exam_preffered= "GMAT + TOEFL/IELTS"
                print("GMAT")
        elif country == "Canada":
            if degree == "MS":
                exam_preffered = "GRE + IELTS"
            elif degree =="MBA":
                exam_preffered = "GMAT + IELTS"   
        else :
            if degree =="MS":
                exam_preffered = "GRE + IELTS/TOEFL"
            elif degree =="MBA":
                exam_preffered = "GMAT + IELTS/TOEFL"   
        #return redirect('profile') 
        #context = {'exam_preffered':exam_preffered} 
        profile_result = ProfileResult(exam_preffered=exam_preffered,username_id=username_id)
        profile_result.save()
        return render(request,'profile.html',{'exam_preffered':exam_preffered})
    return render(request,'profile.html')

        #profile_r = ProfileResult.objects.get()
       # return render(request,'main_forms.html')   




#RESOURCES AND PDF DOWNLOAD



def gre_resources(request):

    return render(request, 'main_resources.html')


def pdfdownload(request, *args, **kwargs):
    #response = HttpResponse(pdf.read())
     if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('./static/PDF/Manhattan 5LBs.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Manhattan_5LBs" 
                content = "inline; filename= Manhattan_5LBs.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename= Manhattan_5LBs.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
def pdfDownload2(request, *args, **kwargs):
    if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/Manhattan Word Problems.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Manhattan_Word_Problems" 
                content = "inline; filename= Manhattan_Word_Problems.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename= Manhattan_Word_Problems.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def pdfDownload3(request, *args, **kwargs):
    if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/word_power_made_easy.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Vocalbulary_word_power" 
                content = "inline; filename= Vocalbulary_word_power.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename= Vocalbulary_word_power.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def pdfDownload4(request, *args, **kwargs):
    if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/GRE_Test_ETS.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Practice_test" 
                content = "inline; filename= Practice_test.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Practice_test.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Gremock1(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/GRE_MockTest_1.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Mock_test1" 
                content = "inline; filename= Mock_test1.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Mock_test1.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Answer_gremock1(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/AnswerKey_MockTest_1.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Answerkey_Mocktest1" 
                content = "inline; filename= Answerkey_Mocktest1.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Answerkey_Mocktest1.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Gremock2(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/GRE_MockTest_3.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Mock_test2" 
                content = "inline; filename= Mock_test2.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Mock_test2.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Answer_gremock2(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/AnswerKey_MockTest_2.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Answerkey_Mocktest2" 
                content = "inline; filename= Answerkey_Mocktest2.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Answerkey_Mocktest2.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Gremock3(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('Static/PDF/GRE_Practice_Test_01.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Mock_test3" 
                content = "inline; filename= Mock_test3.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Mock_test3.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Answer_gremock3(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('./static/18.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Answerkey_Mocktest3" 
                content = "inline; filename= Answerkey_Mocktest3.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Answerkey_Mocktest3.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Gremock4(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('./static/PDF/GRE_Practice_Test_02.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Mock_test4" 
                content = "inline; filename= Mock_test4.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Mock_test4.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

def Answer_gremock4(request, *args, **kwargs):
    #if request.method == 'POST':
        #response['Content-Disposition'] = 'attachment;filename=file.pdf'
        with open('./static/20.pdf', 'rb') as pdf:
            if pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                filename = " Answerkey_Mocktest4" 
                content = "inline; filename= Answerkey_Mocktest4.pdf" 
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=Answerkey_Mocktest4.pdf"
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")


def resources_cat(request):
     return render(request,'resources_cat.html')

def resources_gate(request):
     return render(request,'resources_gate.html')

def resources_gmat(request):
    return render(request,'resources_gmat.html')

def resources_ielts(request):
    return render(request,'resources_ielts.html')

def resources_toefl(request):
    return render(request,'resources_toefl.html')



#UNIVERSITY FINDER


def university_gre(request):

    if request.method == 'POST':
        gre_score=request.POST['field1']
        academics=request.POST['field2']
        course=request.POST['field3']

        if((gre_score >='260') &  (gre_score<='340')): 
       
            if ((course == "CS") | (course == "IS") | (course == "EE") | (course == "Mechanical") | (course == "Chemical") | (course == "Civil")):
            
            
                    if (gre_score >= '325' ) & (academics >= '80'):
                        GRE_university= Gre_CSEECE.objects.filter(flag__in=[1,2])
                        for i in GRE_university.all():
                            context={
                                'GRE_university':GRE_university
                                    }
        
                        return render(request,'main_university_finder.html',context)
                    elif ((gre_score >= '315') & (gre_score <= '324')) & ((academics >= '70') & (academics <= '85') ):
                
                            GRE_university = Gre_CSEECE.objects.filter(flag=2)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)

                    elif ((gre_score >= '300') & (gre_score <= '314')) & ((academics >= '60') & (academics <= '85') ):
                
                            GRE_university = Gre_CSEECE.objects.filter(flag=3)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)

                    elif ((gre_score <= '299')) & ( (academics <= '75') ):
                
                            GRE_university = Gre_CSEECE.objects.filter(flag=4)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)

            elif((course == "WC") | (course == "DataScience")):

                    if (gre_score >= '325') & (academics >= '80'):
                        GRE_university= Gre_MechanicalCivil.objects.filter(flag=1)
                        for i in GRE_university.all():
                            context={
                                'GRE_university':GRE_university
                                    }
        
                        return render(request,'main_university_finder.html',context)
                    elif ((gre_score >= '315') & (gre_score <= '324')) & ((academics >= '70') & (academics <= '85') ):
                
                            GRE_university = Gre_MechanicalCivil.objects.filter(flag=2)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)

                    elif ((gre_score >= '300') & (gre_score <= '314')) & ((academics >= '60') & (academics <= '85') ):
                
                            GRE_university = Gre_MechanicalCivil.objects.filter(flag=3)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)

                    elif ((gre_score <= '299')) & ( (academics <= '75') ):
                
                            GRE_university = Gre_MechanicalCivil.objects.filter(flag=4)
                            for i in GRE_university.all():
                                context={
                                    'GRE_university':GRE_university
                                    }
        
                            return render(request,'main_university_finder.html',context)     

        else: 
            print('enter valid score')
            messages.error(request,'Enter Valid Score')
    
    return render(request,'main_university_finder.html')

def university_cat(request):

    return render(request,'main_university_finder_CAT.html')

def university_gate(request):

    return render(request,'main_university_finder_GATE.html')

def university_gmat(request):

    return render(request,'main_university_finder_GMAT.html')


#SCORE EVALUATION

def score_evaluation_page(request):

    return render(request,"score_evaluation_GRE.html")

def score_evaluation_gate(request):
    return render(request,'score_evaluation_GATE.html')

def score_evaluation_gmat(request):
    return render(request,'score_evaluation_GMAT.html')

def score_evaluation_cat(request):
    return render(request,'score_evaluation_CAT.html')


def submit_score1_GRE(request):
   
    if request.method=='POST':
         user=request.user
         username_id=user.username
         if Score1_Evaluation_GRE.objects.filter(username_id=username_id).exists():
            return redirect ('grescore')
         else:
           
             score1= request.POST['score1']
             submit_score1_GRE = Score1_Evaluation_GRE(score1=score1, username_id=username_id)
             submit_score1_GRE.save()

    else: 
         return redirect(request, 'score_evaluation_GRE.html')

    return render(request,'score_evaluation_GRE.html')

def submit_score2_GRE(request):
    if request.method=='POST':
         user=request.user
         username_id=user.username
       
         if Score2_Evaluation_GRE.objects.filter(username_id=username_id).exists():
             return redirect ('grescore2')
         else:
             score2= request.POST['score2']
             submit_score2_GRE = Score2_Evaluation_GRE(score2=score2, username_id=username_id)
             submit_score2_GRE.save()

    else: 
         return redirect(request, 'score_evaluation_GRE.html')
    return render(request,'score_evaluation_GRE.html')

def submit_score3_GRE(request):
    if request.method=='POST':
         user=request.user
         username_id=user.username
        
         if Score3_Evaluation_GRE.objects.filter(username_id=username_id).exists():
             return redirect ('grescore3')
         else:
             score3= request.POST['score3']
             submit_score3_GRE = Score3_Evaluation_GRE(score3=score3, username_id=username_id)
             submit_score3_GRE.save()

    else:
        return redirect(request, 'score_evaluation_GRE.html') 
    return render(request, 'score_evaluation_GRE.html')
    #return render(request,'score_evaluation_GRE.html')

def submit_score4_GRE(request):
    if request.method=='POST':
         user=request.user
         username_id=user.username
        
         if Score4_Evaluation_GRE.objects.filter(username_id=username_id).exists():
             return redirect ('grescore4')
         else:
             score4= request.POST['score4']
             submit_score4_GRE = Score4_Evaluation_GRE(score4=score4, username_id=username_id)
             submit_score4_GRE.save()
             
    else: 
        return redirect(request, 'score_evaluation_GRE.html')
    return render(request, 'score_evaluation_GRE.html')
    #return render(request,'score_evaluation_GRE.html')

def score1(request):
    user=request.user
    username_id=user.username
    score_1= Score1_Evaluation_GRE.objects.get(username_id=username_id)
    context = {'score_1':score_1}
    return render(request,'score_evaluation_GRE.html',context)

def score2(request):
    user=request.user
    username_id=user.username
    score_2= Score2_Evaluation_GRE.objects.get(username_id=username_id)
    context = {'score_2':score_2}
    return render(request,'score_evaluation_GRE.html',context)


def score3(request):
    user=request.user
    username_id=user.username
    score_3= Score3_Evaluation_GRE.objects.get(username_id=username_id)
    context = {'score_3':score_3}
    return render(request,'score_evaluation_GRE.html',context)

def score4(request):
    user=request.user
    username_id=user.username
    score_4= Score4_Evaluation_GRE.objects.get(username_id=username_id)
    context = {'score_4':score_4}
    return render(request,'score_evaluation_GRE.html',context)



def evaluate_GRE(request):
    user=request.user
    username_id=user.username
    s1 = Score1_Evaluation_GRE.objects.get(username_id=username_id)
    s2 = Score2_Evaluation_GRE.objects.get(username_id=username_id)
    s3 = Score3_Evaluation_GRE.objects.get(username_id=username_id)
    s4 = Score4_Evaluation_GRE.objects.get(username_id=username_id)

    score1 = s1.score1
    score2 = s2.score2
    score3 = s3.score3
    score4 = s4.score4
    estimated_score = int (((score1)+(score2)+(score3) +(score4))/4) 
    #score_result = Score_Result_GRE(score_evaluated=estimated_score,username_id=username_id)
    #score_result.save();
    print(estimated_score)

    
    if Score_Result_GRE.objects.filter(username_id=username_id).exists():
        gre_result = Score_Result_GRE.objects.get(username_id=username_id)

        context ={
                    'gre_result': gre_result
            }
        return render(request, 'score_evaluation_GRE.html',context)

    else:
        score_result = Score_Result_GRE(score_evaluated=estimated_score,username_id=username_id)
        score_result.save();
        gre_result = Score_Result_GRE.objects.get(username_id=username_id)

        context ={
                    'gre_result': gre_result
            }

        return render(request, 'score_evaluation_GRE.html',context)



###---------------------------------EXAMINATIONS------------------------------

def grehome(request):
    return render(request,'grehome.html')

def CAThome(request):
    return render(request,'CAThome.html')

def gmathome(request):
    return render(request,'gmathome.html')

def IELTShome(request):
    return render(request,'IELTShome.html')

def gatehome(request):
    return render(request,'gatehome.html')

def toeflhome(request):
    return render(request,'toeflhome.html')

def catdilr(request):
    return render(request,'CATdilr.html')

def catquant(request):
    return render(request,'catquant.html')

def catverbal(request):
    return render(request,'catverbal.html')

def gmatawa(request):
    return render(request,'gmatAWA.html')

def gmatir(request):
    return render(request,'gmatIR.html')

def gmatquant(request):
    return render(request,'gmatquant.html')

def gmatverbal(request):
    return render(request,'gmatverbal.html')

def greawa(request):
    return render(request,'greAWA.html')

def grequant(request):
    return render(request,'grequant.html')

def greverbal(request):
    return render(request,'greverbal.html')

def ieltslistening(request):
    return render(request,'ieltslistening.html')

def ieltspeaking(request):
    return render(request,'ieltspeaking.html')

def ieltsreading(request):
    return render(request,'ieltsreading.html')

def ieltswriting(request):
    return render(request,'ieltswriting.html')


### My profile

def myprofile(request):
    return render(request,'profile.html')

def aboutus(request):
    return render(request,'about_us.html')
    
########QUIZ##############

def quiz1(request):
    return render(request,'quiz1.html')

def quiz2(request):
    return render(request,'quiz2.html')

def quiz3(request):
    return render(request,'quiz3.html')

def quiz4(request):
    return render(request,'quiz4.html')

def quiz5(request):
    return render(request,'quiz5.html')

def quiz6(request):
    return render(request,'quiz6.html')

def quiz7(request):
    return render(request,'quiz7.html')


def test_result(request):
    current_user = request.user
    username_id = current_user.id

    if Score_Result_GRE.objects.filter(username_id=username_id).exists():
        instance = Score_Result_GRE.objects.get(username_id=id)
        form = Form_profileresult(instance=instance)
        context = {'instance':instance,}
        return render(request,'profile.html')

import pandas as pd
import pickle
import joblib, os

def UniversityList(request):
    if request.method == "POST":
        GRE_Score = float(request.POST['field1'])
        CGPA = float(request.POST['field2'])
        degree = request.POST['field3']
        SOP = float(request.POST['field4'])
        LOR = float(request.POST['field5'])
        Research = float(request.POST['field6'])
        TOEFL_Score = float(request.POST['field7'])
        l1 = [GRE_Score] 
        l2 = [TOEFL_Score] 
        l3 = [SOP]
        l4 = [LOR]
        l5 = [CGPA]
        l6 = [Research]
        # print(l1)

        df = pd.DataFrame(list(zip(l1, l2, l3, l4, l5, l6)))
        df.columns = ['GRE_Score', 'TOEFL_Score', 'SOP', 'LOR', 'CGPA', 'Research']
        print(df)
        mdl = joblib.load('./load_model.pkl')
        ratings = mdl.predict(df)
        print(ratings)

        dfUni = pd.read_csv('./datasets/University_list.csv',
                            error_bad_lines=False, sep='\t')
        print(dfUni.head())
        print(dfUni['university name'])

        dfUni = pd.DataFrame(
            dfUni.values, columns=['University', 'location', 'fees', 'flag'])

        print(type(dfUni))

        dfUni['flag'].replace({1: 5, 2: 4, 4: 2, 5: 1},  inplace=True)

        print(dfUni.head())
        dfFilter = dfUni[dfUni['flag'] <= ratings[0]]

        # dfFilter = list(dfFilter)

        print((dfFilter))

        return render(request,'main_university_finder.html', {'dfFilter' : dfFilter})

    return render(request, 'main_university_finder.html')
