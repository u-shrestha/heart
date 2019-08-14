import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heart = pd.read_csv('D:\Zzz Project\AAA practise\disease_prediction\prediction\heart.csv')
wd=0.4

plt.figure(figsize=(10,8))
plt.title('Correlation Heatmap of Attributes')
sns.heatmap(heart.corr(),annot=True,cmap='YlGnBu',fmt='.2f',linewidths=2)
plt.savefig('..\.\static\graph\heatmap.png')
plt.show()
plt.close()

# plt.figure(figsize=(10,10))
# sns.heatmap(heart.corr(),annot=True,fmt='.1f')
# plt.savefig('..\.\static\graph\heatmap.png')
# plt.show()
# plt.close()

pd.crosstab(heart.age,heart.target).plot(kind="bar",figsize=(20,6), width=wd, color=['#362bff','#ff322b' ])
plt.legend(['No Heart Disease','Heart Disease'])
plt.title('Heart Disease Frequency for Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('..\.\static\graph\Age.png')
plt.show()
plt.close()

pd.crosstab(heart.sex,heart.target).plot(kind="bar",figsize=(4,6), width=wd, color=['#64a9d1','#f59da7' ])
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.xticks(rotation=0)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.savefig('..\.\static\graph\Sex.png')
plt.show()
plt.close()

pd.crosstab(heart.slope,heart.target).plot(kind="bar",figsize=(8,8), width=wd, color=['#64a9d1','#f59da7'])
plt.title('Heart Disease Frequency for Slope')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.xlabel('The Slope of The Peak Exercise ST Segment ( 0 = upsloping, 1 = flat, 2 = downsloping)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency')
plt.savefig('..\.\static\graph\Slope.png')
plt.show()
plt.close()


pd.crosstab(heart.fbs,heart.target).plot(kind="bar",figsize=(6,6), width=wd, color=['#138bbf','#cc7e9d' ])
plt.title('Heart Disease Frequency According To FBS')
plt.xlabel('FBS - (Fasting Blood Sugar > 120 mg/dl) (1 = true; 0 = false)')
plt.xticks(rotation = 0)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency of Disease or Not')
plt.savefig('..\.\static\graph\Fbs.png')
plt.show()
plt.close()

pd.crosstab(heart.cp,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Chest Pain Type')
plt.xlabel('Chest Pain Type ( 0= typical angina, 1= atypical angina, 2= non-anginal pain, 3= asymptotic)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\chestpain.png')
plt.show()
plt.close()

pd.crosstab(heart.trestbps,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Resting Blood Pressure')
plt.xlabel('Resting Blood Pressure')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\pressure.png')
plt.show()
plt.close()

pd.crosstab(heart.chol,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Serum Cholesterol')
plt.xlabel('Serum Cholesterol')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\chol.png')
plt.show()
plt.close()


pd.crosstab(heart.restecg,heart.target).plot(kind="bar",figsize=(8,6), width= wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Resting ECG')
plt.xlabel('Resting ECG  (0 = normal, 1 = having ST-T wave abnormality, 2 = left ventricular hypertrophy)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\ecg.png')
plt.show()
plt.close()

pd.crosstab(heart.thalach,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Max heart rate achieved')
plt.xlabel('Max heart rate achieved (bpm)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\h_rate.png')
plt.show()
plt.close()

pd.crosstab(heart.exang,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Exercise Induced Angina')
plt.xlabel('Exercise induced angina ( 1 = yes, 0 = no)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\exercise.png')
plt.show()
plt.close()

pd.crosstab(heart.oldpeak,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To ST Depression Induced by Exercise Relative to Rest')
plt.xlabel('ST depression induced by exercise relative to rest')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\ST_exer.png')
plt.show()
plt.close()

pd.crosstab(heart.ca,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Number of Major Vessels (0-3) colored by Fluoroscopy')
plt.xlabel('Number of major vessels (0-3) colored by fluoroscopy')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\Vessels.png')
plt.show()
plt.close()

pd.crosstab(heart.thal,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Thalassemia')
plt.xlabel('Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('..\.\static\graph\Thal.png')
plt.show()
plt.close()



plt.scatter(x=heart.age[heart.target==1], y=heart.thalach[(heart.target==1)], c="red")
plt.scatter(x=heart.age[heart.target==0], y=heart.thalach[(heart.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.show()

