from django.forms import ModelForm
from django import forms
from .models import ProfileEvaluation,Score_Result_GRE

Name_Choice=[('rutvi','Rutvi'),
              ('prima','Prima')]

Degree_Choice=[('MBA','Masters in Business Administration'),
                ('MS','Masters in Science and Techonology')]

AOI_choice=[('CS','Computer Science'),('DS','Data Science'),('WC','Wireless Communication'),('IS','Information Systems'),
            ('ENV','Environmental Engineering'),('CE','Chemical Enigineering'),('M','Logistic and supply chain managemnet'),
            ('F','Masters in Finance'),('M1','Marketing Management'),('HR','Human Resources Management'),('E','Enterpreneurship'),
            ('IB','International Business Management')]
Country_choice=[('India','India'),('USA','United States of America'),('Canada','Canada'),('Australia','Australia'),
                ('Germany','Germany'),('London','London')]
class Form_profile(ModelForm):
    
    name= forms.CharField(label='Name',required=True)
    dob= forms.DateTimeField(label='Date of birth',widget= forms.TextInput
                           (attrs={'placeholder':'dd/mm/yyyy format'}),required=True)
    contact = forms.IntegerField(label = 'Contact Number',required=True)
    
    country = forms.CharField(label='Which Country are you planning to prepare for higher studies?',widget=forms.Select(choices=Country_choice),required=True)
    budget = forms.IntegerField(label='Your Yearly Budget',required=True)
    degree = forms.CharField(label='Which Degree are you aimming for ?',widget=forms.Select(choices=Degree_Choice),required=True)
    AOI_1 = forms.CharField(label='Select your first preffered area of interest',widget=forms.Select(choices=AOI_choice),required=True)
    AOI_2 = forms.CharField(label='Select your second preffered area of interest',widget=forms.Select(choices=AOI_choice),required=True)
    percentage_10 = forms.IntegerField(label='Enter your 10th percentage',required='True')
    percentage_12 = forms.IntegerField(label='Enter your 12th percentage',required='True')
    percentage_undergrad = forms.FloatField(label='Enter your Graduate/Under-Graduate percentage',required='True')
    backlogs = forms.IntegerField(label='Enter the number of backlogs',required=True)
        

    class Meta:
        model = ProfileEvaluation
        fields=[
        'name','dob','contact','country','budget','degree','AOI_1','AOI_2','percentage_10','percentage_12','percentage_undergrad',
        'backlogs'
        ]

class Form_profileresult(ModelForm):

        score_evaluated = forms.IntegerField()

        class Meta:
            model = Score_Result_GRE
            fields=['score_evaluated']
        
        #widget={'text':forms.TextInput( attrs={'placeholder':'Enter your name'})}
        #.CharField(label='Enter your name', widget=forms.Select(choices=Name_CHOICES))
        #widget=forms.TextInput(attrs={"placeholder":"Enter your name"})