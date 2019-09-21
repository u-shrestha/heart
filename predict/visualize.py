import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heart = pd.read_csv('F:\\AI\heart\predict\heart.csv')
wd=0.4

plt.figure(figsize=(10,8))
sns.heatmap(heart.corr(),annot=True,cmap='YlGnBu',fmt='.2f',linewidths=2)
plt.show()

plt.title('Distibution by age')
sns.set()
heart[heart.target==1].age.hist(bins=20)
heart[heart.target==0].age.hist(bins=20)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.xlabel('age')
plt.savefig('Age.png')
plt.show()
plt.close()

pd.crosstab(heart.sex,heart.target).plot(kind="bar",figsize=(4,6), width=wd, color=['#64a9d1','#f59da7' ])
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.xticks(rotation=0)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.savefig('Sex.png')
plt.show()
plt.close()

pd.crosstab(heart.cp,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Chest Pain Type')
plt.xlabel('Chest Pain Type ( 0= typical angina, 1= atypical angina, 2= non-anginal pain, 3= asymptotic)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('chestpain.png')
plt.show()
plt.close()

plt.title('Distibution by Resting Blood Pressure')
sns.set()
heart[heart.target==1].trestbps.hist(bins=20)
heart[heart.target==0].trestbps.hist(bins=20)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.xlabel('Resting Blood Pressure (mmHg)')
plt.savefig('resting_press.png')
plt.show()
plt.close()

plt.title('Distibution by Serum Cholesterol')
sns.set()
heart[heart.target==1].chol.hist(bins=20)
heart[heart.target==0].chol.hist(bins=20)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.xlabel('Serum Cholesterol (mg/dl)')
plt.savefig('se_chol.png')
plt.show()
plt.close()

pd.crosstab(heart.fbs,heart.target).plot(kind="bar",figsize=(6,6), width=wd, color=['#138bbf','#cc7e9d' ])
plt.title('Heart Disease Frequency According To FBS')
plt.xlabel('FBS - (Fasting Blood Sugar > 120 mg/dl) (1 = yes; 0 = no)')
plt.xticks(rotation = 0)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency of Disease or Not')
plt.savefig('Fbs.png')
plt.show()
plt.close()

pd.crosstab(heart.fbs,heart.target).plot(kind="bar",figsize=(6,6), width=wd, color=['#138bbf','#cc7e9d' ])
plt.title('Heart Disease Frequency According To Resting ECG')
plt.xlabel('Resting ECG (0 = normal; 1 = abnormal)')
plt.xticks(rotation = 0)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency of Disease or Not')
plt.savefig('restecg.png')
plt.show()
plt.close()

plt.title('Distibution by Maximum heart rate achieved')
sns.set()
heart[heart.target==1].thalach.hist(bins=30)
heart[heart.target==0].thalach.hist(bins=30)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.xlabel('Max heart rate achieved')
plt.savefig('max_hr.png')
plt.show()
plt.close()

pd.crosstab(heart.exang,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Exercise Induced Angina')
plt.xlabel('Exercise induced angina ( 1 = yes, 0 = no)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('exercise.png')
plt.show()
plt.close()

plt.title('Distibution by ST depression induced by exercise relative to rest')
sns.set()
heart[heart.target==1].oldpeak.hist(bins=20)
heart[heart.target==0].oldpeak.hist(bins=20)
plt.legend(["No Heart Disease", "Heart Disease"])
plt.ylabel('Frequency')
plt.xlabel('ST depression induced by exercise relative to rest')
plt.savefig('oldpeak.png')
plt.show()
plt.close()

pd.crosstab(heart.slope,heart.target).plot(kind="bar",figsize=(8,8), width=wd, color=['#64a9d1','#f59da7'])
plt.title('Heart Disease Frequency for Slope')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.xlabel('The Slope of The Peak Exercise ST Segment ( 0 = upsloping, 1 = flat, 2 = downsloping)')
plt.xticks(rotation = 0)
plt.ylabel('Frequency')
plt.savefig('Slope.png')
plt.show()
plt.close()

pd.crosstab(heart.ca,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Number of Major Vessels (0-3) colored by Fluoroscopy')
plt.xlabel('Number of major vessels (0-3) colored by fluoroscopy')
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('Vessels.png')
plt.show()
plt.close()

pd.crosstab(heart.thal,heart.target).plot(kind="bar",figsize=(8,6), width=wd, color=['#a2cffe','#f49ac2' ])
plt.title('Heart Disease Frequency According To Thalassemia')
plt.xlabel('Thalassemia (1 = normal, 2 = alpha, 3 = beta)' )
plt.xticks(rotation = 0)
plt.ylabel('Frequency of Disease or Not')
plt.legend(["No Heart Disease", "Heart Disease"])
plt.savefig('Thal.png')
plt.show()
plt.close()