import uuid
from django.db import models

# Create your models here.

class HealthData(models.Model):

    
    class Sex(models.IntegerChoices):
        male = (1, 'MALE')
        female = (0, 'FEMALE')


    class Diseases(models.TextChoices):
        _none = ('NONE', "NONE")
        asthma = ('ASTHMA', 'Asthma')
        kidney_disease = ('KIDNEY DISEASE', 'Kidney Disease')
        skin_disease = ('SKIN DISEASE', 'Skin Disease')



    class GeneralHealth(models.IntegerChoices):
        exellent = (4, 'EXCELLENT')
        very_good = (3, 'VERY GOOD')
        good = (2, 'GOOD')
        fair = (1, 'FAIR')
        poor = (0, 'POOR')
    
    class AgeCategory(models.IntegerChoices):
        a = (0, '18-24')
        b = (1, '25-29')
        c = (2, '30-34')
        d = (3, '35-39')
        e = (4, '40-44')
        f = (5, '45-49')
        g = (6, '50-54')
        h = (7, '55-59')
        i = (8, '60-64')
        j = (9, '65-69')
        k = (10, '70-74')
        m = (11, '75-79')
        l = (12, '80+')

    class Races(models.IntegerChoices):
        white = (0, "WHITE")
        black = (1, 'BLACK')
        hispanic = (2, 'HISPANIC')
        asian = (3, 'ASIAN')
        natives = (4, 'NATIVES')
        other = (5, 'OTHERS')


    health_data_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    # belongs_to = 


    heart_disease = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    alcohol_drinking = models.BooleanField(default=False)
    stroke = models.BooleanField(default=False)
    physical_health = models.SmallIntegerField()
    mental_health = models.SmallIntegerField()
    diff_walking = models.BooleanField(default=False)
    
    sex = models.SmallIntegerField(choices=Sex, default=Sex.male)
    age = models.SmallIntegerField(choices=AgeCategory, default=AgeCategory.a)

    race = models.SmallIntegerField(choices=Races, default=Races.white)

    diaobitic = models.BooleanField(default=False)
    physical_activity = models.BooleanField(default=False)
    sleep_time = models.SmallIntegerField()

    general_health = models.SmallIntegerField(choices=GeneralHealth)

    # Final Disease
    disease = models.CharField(max_length=30, choices=Diseases, default=Diseases._none)
    


