from django.shortcuts import render, HttpResponse
from .forms import HealthDataForm
from .model_final import user_input

sample_data = {
    'heart_disease': 'heart_disease',
    'skin_cancer': 'skin_cancer', 
    'asthma': 'asthma',
    'kidney_disease': 'kidney_disease'
}

sample_description = {
    'None': 'You are in good health and please maintain this new health',
    'heart_disease': 'You may have Heart Disease, Heart disease encompasses various conditions affecting the heart\'s structure and function, including coronary artery disease, heart attacks, and arrhythmias. Risk factors include high blood pressure, high cholesterol, smoking, obesity, and diabetes. Symptoms can range from chest pain to shortness of breath, and prevention focuses on lifestyle changes and medical management.',
    'skin_cancer': 'Skin cancer arises from abnormal growth of skin cells, often due to UV exposure. The main types are basal cell carcinoma, squamous cell carcinoma, and melanoma. Risk factors include fair skin, a history of sunburns, and tanning bed use. Early detection is crucial, with symptoms like unusual moles or growths.',
    'asthma': 'Asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to difficulty breathing, wheezing, coughing, and chest tightness. Triggers include allergens, exercise, and pollution. While there is no cure, asthma can be managed with medications and lifestyle adjustments to minimize symptoms and flare-ups.',
    'kidney_disease': 'Kidney disease refers to a range of conditions affecting kidney function, including chronic kidney disease and acute kidney injury. Causes include diabetes, high blood pressure, and infections. Symptoms may include fatigue, swelling, and changes in urine output. Early detection and management are crucial to slowing progression and preventing complications.',
}


# Create your views here.
def predictor(request):
    form = HealthDataForm()

    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        pd = request.POST
        print(request.POST)

        physical_health = int(pd['physical_health'])
        mental_health = int(pd['mental_health'])
        sex = int(pd['sex'])
        age = int(pd['age'])
        sleep_time = int(pd['sleep_time'])
        general_health = int(pd['general_health'])
        race = int(pd['race'])

        smoking = 1 if pd.get('smoking') else 0
        alcohol = 1 if pd.get('alcohol_drinking') else 0
        stroke = 1 if pd.get('stroke') else 0
        diff_walking = 1 if pd.get('diff_walking') else 0
        diaobitic = 1 if pd.get('diaobitic') else 0
        physical_activity = 1 if pd.get('physical_activity') else 0        
        print(physical_activity, physical_health, sex, age, sleep_time, general_health, race, smoking, alcohol, stroke, diff_walking, diaobitic)
        if form.is_valid():

            res = user_input(
                smoke=smoking,
                alch=alcohol,
                stroke=stroke,
                phyHel=physical_health,
                mentHel=mental_health,
                diffWalk=diff_walking,
                sex=sex,
                ageCat=age,
                race=race,
                diab=diaobitic,
                phyAct=physical_activity,
                genHel=general_health,
                sleep=sleep_time
            )
            print(type(res), res)
            print('form is valid and process will be done here')

            return result(request,  res)
        
        else:
            print('form is not valid')


    context = {
        'form': form
    }

    return render(request, 'diseasepredictor/healthform.html', context=context)



def result(request, results):

    heart = results[0] * 100
    kidney = results[1]*100
    skin = results[2]*100
    asthma = results[3]*100

    context = {
        'heart': heart,
        'asthma': asthma,
        'kidney': kidney,
        'skin': skin,
    }

    return render(request, 'diseasepredictor/result.html', context=context)



