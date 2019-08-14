from django.shortcuts import render
from . import model

def home(request):
    return render(request, 'index.html')

def result(request):
    Pclass = int(request.GET['Pclass'])
    Sex = int(request.GET['Sex'])
    Age = int(request.GET['Age'])
    SibSp = int(request.GET['SibSp'])
    Parch = int(request.GET['Parch'])
    Fare = float(request.GET['Fare'])
    Embarked = int(request.GET['Embarked'])
    Title = int(request.GET['Title'])
    user_input = [[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    prediction = model.predict(user_input)
    return render(request, 'result.html', {'home_input':prediction})
