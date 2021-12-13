from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    #path('',views.home , name = 'home'),
    #path('add',views.add, name = 'add'), 
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('home',views.add,name='home'),
    path('profile',views.Evalprofile ,name='profile'),
    path('checkeval',views.check_profile,name='checkeval'),
    #path('Evalprofile',views.Evalprofile,name='Evalprofile'),
    #path('university',views.university,name='university'),
    path('gre_resources',views.gre_resources,name='gre_resources'),
    path('resources_cat',views.resources_cat,name='resources_cat'),
    path('resources_gmat',views.resources_gmat,name='resources_gmat'),
    path('resources_gate',views.resources_gate,name='resources_gate'),
    path('resources_ielts',views.resources_ielts,name='resources_ielts'),
    path('resources_toefl',views.resources_toefl,name='resources_toefl'),

    #path('dummy',views.quiz,name='dummy'),
    path('updateprofile',views.UpdateProfile,name='updateprofile'),
    # path('update_profile',views.update,name='update_profile'),
    path('profile_result',views.profile_result,name='profile_result'),
    #path('download_b',views.download,name='download_b'),
    path('download_1',views.pdfdownload,name='download_1'),
    path('download_2',views.pdfDownload2,name='download_2'),
    path('download_3',views.pdfDownload3,name='download_3'),
    path('download_4',views.pdfDownload4,name='download_4'),
    path('download_mock1',views.Gremock1,name='download_mock1'),
    path('download_ans_mock1',views.Answer_gremock1,name='download_ans_mock1'),
    path('download_mock2',views.Gremock2,name='download_mock2'),
    path('download_ans_mock2',views.Answer_gremock2,name='download_ans_mock2'),
    path('download_mock3',views.Gremock3,name='download_mock3'),
    path('download_ans_mock3',views.Answer_gremock3,name='download_ans_mock3'),
    path('download_mock4',views.Gremock4,name='download_mock4'),
    path('download_ans_mock4',views.Answer_gremock4,name='download_ans_mock4'),
    

    
    path('greuni', views.UniversityList, name='greuni'),
    path('greunicat',views.university_cat,name='greunicat'),
    path('greunigate',views.university_gate,name='greunigate'),
    path('greunigmat',views.university_gmat,name='greunigmat'),

    path('grescore',views.score1,name='grescore'),
    path('grescore2',views.score2,name='grescore2'),
    path('grescore3',views.score3,name='grescore3'),
     path('grescore4',views.score4,name='grescore4'),
    path('score_evaluation_page',views.score_evaluation_page,name='score_evaluation_page'),
    path('submit_score1_GRE',views.submit_score1_GRE,name='submit_score1_GRE'),
    path('submit_score2_GRE',views.submit_score2_GRE,name='submit_score2_GRE'),
    path('submit_score3_GRE',views.submit_score3_GRE,name='submit_score3_GRE'),
    path('submit_score4_GRE',views.submit_score4_GRE,name='submit_score4_GRE'),
    path('evaluate_GRE',views.evaluate_GRE,name='evaluate_GRE'),
    path('score_evaluation_gate',views.score_evaluation_gate,name='score_evaluation_gate'),
    path('score_evaluation_gmat',views.score_evaluation_gmat,name='score_evaluation_gmat'),
    path('score_evaluation_cat',views.score_evaluation_cat,name='score_evaluation_cat'),

    path('reset_password',auth_views.PasswordResetView.as_view(template_name="password_reset.html" ),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),

#####--Examinations-------

    path('grehome',views.grehome,name='grehome'),
    path('cathome',views.CAThome,name='cathome'),
    path('gmathome',views.gmathome,name='gmathome'),
    path('ieltshome',views.IELTShome,name='ieltshome'),
    path('gatehome',views.gatehome,name='gatehome'),
    path('toeflhome',views.toeflhome,name='toeflhome'),

    path('catdilr',views.catdilr,name='catdilr'),
    path('catquant',views.catquant,name='catquant'),
    path('catverbal',views.catverbal,name='catverbal'),

    path('gmatawa',views.gmatawa,name='gmatawa'),
    path('gmatir',views.gmatir,name='gmatir'),
    path('gmatquant',views.gmatquant,name='gmatquant'),
    path('gmatverbal',views.gmatverbal,name='gmatverbal'),

    path('greawa',views.greawa,name='greawa'),
    path('grequant',views.grequant,name='grequant'),
    path('greverbal',views.greverbal,name='greverbal'),

    path('ieltslistening',views.ieltslistening,name='ieltslistening'),
    path('ieltswriting',views.ieltswriting,name='ieltswriting'),
    path('ieltspeaking',views.ieltspeaking,name='ieltspeaking'),
    path('ieltsreading',views.ieltsreading,name='ieltsreading'),

    path('myprofile',views.myprofile,name='myprofile'),
     path('aboutus',views.aboutus,name='aboutus'),

     path('quiz1',views.quiz1,name='quiz1'),
    path('quiz2',views.quiz2,name='quiz2'),
    path('quiz3',views.quiz3,name='quiz3'),
    path('quiz4',views.quiz4,name='quiz4'),
    path('quiz5',views.quiz5,name='quiz5'),
    path('quiz6',views.quiz6,name='quiz6'),
    path('quiz7',views.quiz7,name='quiz7'),
    
]
