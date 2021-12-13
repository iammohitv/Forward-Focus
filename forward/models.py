from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Registration(models.Model):

    first_name= models.CharField( max_length=100)
    last_name= models.CharField( max_length=100)
    username = models.CharField(max_length=100,primary_key=True,unique=True)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class ProfileEvaluation(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    contact = models.BigIntegerField()
    country =models.CharField(max_length=100)
    budget = models.IntegerField()
    degree = models.CharField(max_length=100)
    AOI_1 = models.CharField(max_length=100)
    AOI_2 = models.CharField(max_length=100)
    percentage_10 = models.IntegerField()
    percentage_12 = models.IntegerField()
    percentage_undergrad = models.IntegerField()
    backlogs = models.FloatField()
    username = models.ForeignKey(Registration, on_delete=models.CASCADE)
    
    
     
class ProfileResult(models.Model):

    #name = models.CharField(max_length=100)
    exam_preffered = models.CharField(max_length=100)
    username = models.ForeignKey(Registration, on_delete=models.CASCADE)
    
class Gre_CSEECE(models.Model):
    
    university_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    fees =     models.IntegerField()
    flag = models.IntegerField()


class Gre_MechanicalCivil(models.Model):

    university_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    fees =     models.IntegerField()
    flag = models.IntegerField()


class Cat(models.Model):
  
    university_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    fees =     models.IntegerField()
    flag = models.IntegerField()

class GREScore(models.Model):

    grescore = models.IntegerField()
    academic_percentage = models.FloatField()
    AOI = models.CharField(max_length=150)

class CATScore(models.Model):

    catscore = models.IntegerField()
    academic_percentage = models.FloatField()
    AOI = models.CharField(max_length=150)

class Dummy(models.Model):

    name = models.CharField(max_length=150)
    number = models.IntegerField()





class Score1_Evaluation_GRE(models.Model):

    score1 = models.IntegerField()
    username = models.ForeignKey(Registration,on_delete=models.CASCADE)

class Score2_Evaluation_GRE(models.Model):

    score2 = models.IntegerField()
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,)

class Score3_Evaluation_GRE(models.Model):

    score3 = models.IntegerField()
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,)

class Score4_Evaluation_GRE(models.Model):

    score4 = models.IntegerField()
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,)

class Score_Result_GRE(models.Model):

    username = models.ForeignKey(Registration,on_delete=models.CASCADE)
    score_evaluated = models.IntegerField()
