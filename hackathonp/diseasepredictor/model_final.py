import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv(r'/home/yubiyuub/yubi/work/programming/hackathon/hackathonp/diseasepredictor/BRFSS_sample.csv')
df = df.dropna()

df['Diabetic'] = df['Diabetic'].replace('No', 0)
df['Diabetic'] = df['Diabetic'].replace('Yes', 1)
df['Diabetic'] = df['Diabetic'].replace('No, borderline diabetes', 2)
df['Diabetic'] = df['Diabetic'].replace('Yes (during pregnancy)', 3)

df['Sex'] = df['Sex'].replace('Male', 1)
df['Sex'] = df['Sex'].replace('Female', 0)

df['GenHealth'] = df['GenHealth'].replace('Poor', 0)
df['GenHealth'] = df['GenHealth'].replace('Fair', 1)
df['GenHealth'] = df['GenHealth'].replace('Good', 2)
df['GenHealth'] = df['GenHealth'].replace('Very good', 3)
df['GenHealth'] = df['GenHealth'].replace('Excellent', 4)

df['Race'] = df['Race'].replace('White', 0)
df['Race'] = df['Race'].replace('Black', 1)
df['Race'] = df['Race'].replace('Hispanic', 2)
df['Race'] = df['Race'].replace('Asian', 3)
df['Race'] = df['Race'].replace('American Indian/Alaskan Native', 4)
df['Race'] = df['Race'].replace('Other', 5)

df['SkinCancer'] = df['SkinCancer'].replace('No', 0)
df['SkinCancer'] = df['SkinCancer'].replace('Yes', 1)

df['HeartDisease'] = df['HeartDisease'].replace('Yes', 1)
df['HeartDisease'] = df['HeartDisease'].replace('No', 0)

df['Smoking'] = df['Smoking'].replace('Yes', 1)
df['Smoking'] = df['Smoking'].replace('No', 0)

df['AlcoholDrinking'] = df['AlcoholDrinking'].replace('Yes', 1)
df['AlcoholDrinking'] = df['AlcoholDrinking'].replace('No', 0)

df['Stroke'] = df['Stroke'].replace('Yes', 1)
df['Stroke'] = df['Stroke'].replace('No', 0)

df['DiffWalking'] = df['DiffWalking'].replace('Yes', 1)
df['DiffWalking'] = df['DiffWalking'].replace('No', 0)

df['PhysicalActivity'] = df['PhysicalActivity'].replace('Yes', 1)
df['PhysicalActivity'] = df['PhysicalActivity'].replace('No', 0)

df['Asthma'] = df['Asthma'].replace('Yes', 1)
df['Asthma'] = df['Asthma'].replace('No', 0)

df['KidneyDisease'] = df['KidneyDisease'].replace('Yes', 1)
df['KidneyDisease'] = df['KidneyDisease'].replace('No', 0)

df['AgeCategory'] = df['AgeCategory'].replace('18-24', 0)
df['AgeCategory'] = df['AgeCategory'].replace('25-29', 1)
df['AgeCategory'] = df['AgeCategory'].replace('30-34', 2)
df['AgeCategory'] = df['AgeCategory'].replace('35-39', 3)
df['AgeCategory'] = df['AgeCategory'].replace('40-44', 4)
df['AgeCategory'] = df['AgeCategory'].replace('45-49', 5)
df['AgeCategory'] = df['AgeCategory'].replace('50-54', 6)
df['AgeCategory'] = df['AgeCategory'].replace('55-59', 7)
df['AgeCategory'] = df['AgeCategory'].replace('60-64', 8)
df['AgeCategory'] = df['AgeCategory'].replace('65-69', 9)
df['AgeCategory'] = df['AgeCategory'].replace('70-74', 10)
df['AgeCategory'] = df['AgeCategory'].replace('75-79', 11)
df['AgeCategory'] = df['AgeCategory'].replace('80 or older', 12)

X = df.drop(columns = ['HeartDisease', 'KidneyDisease', 'SkinCancer', 'Asthma'])
y = df[['HeartDisease', 'KidneyDisease', 'SkinCancer', 'Asthma']]

# standardizing the data
mean = X.sum() / len(X)
var = ((X - mean) ** 2).sum() / len(X)
std_dev = var ** 0.5
X_scaled = (X - mean) / std_dev

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Input
from tensorflow.keras.optimizers import Adam

model = Sequential()
model.add(Input(shape=(13,)))

# First block
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))

# Second block
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))

# Third block
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))

# Output layer
model.add(Dense(4, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_scaled, y, epochs = 10, batch_size = 32, validation_split=0.2)

def user_input(smoke, alch, stroke, phyHel, mentHel, diffWalk, sex, ageCat, race, diab, phyAct, genHel, sleep):
    input_dict = dict(zip(('Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
       'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic',
       'PhysicalActivity', 'GenHealth', 'SleepTime'),([smoke], [alch], [stroke], [phyHel], [mentHel], [diffWalk], [sex], [ageCat], [race], [diab], [phyAct], [genHel], [sleep])))
    
    converted_input = pd.DataFrame(input_dict)
    converted_input_scaled = (converted_input - mean) / std_dev
    final = converted_input_scaled.iloc[0].tolist()

    new_inp = np.array([final])
    predictions = model.predict(new_inp)

    return predictions[0]