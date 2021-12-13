from django.contrib import admin
from .models import ProfileEvaluation,ProfileResult,Registration,Dummy,Gre_CSEECE,Gre_MechanicalCivil,Cat,GREScore,CATScore,Score1_Evaluation_GRE,Score2_Evaluation_GRE,Score3_Evaluation_GRE,Score4_Evaluation_GRE,Score_Result_GRE
# Register your models here.

admin.site.register(Registration)
admin.site.register(ProfileEvaluation)
admin.site.register(ProfileResult)
admin.site.register(Dummy)
admin.site.register(Gre_CSEECE)
admin.site.register(Gre_MechanicalCivil)
admin.site.register(Cat)
admin.site.register(GREScore)
admin.site.register(CATScore)
admin.site.register(Score1_Evaluation_GRE)
admin.site.register(Score2_Evaluation_GRE)
admin.site.register(Score3_Evaluation_GRE)
admin.site.register(Score4_Evaluation_GRE)
admin.site.register(Score_Result_GRE)