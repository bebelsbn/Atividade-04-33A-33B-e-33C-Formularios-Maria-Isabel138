from django.shortcuts import render, redirect
from .models import Hobbies, Learn


def home(request):
    hobbies = Hobbies.objects.all()
    learn = Learn.objects.all()
    print(hobbies)
    return render(request,
                  "home.html",
                  context={
                      "hobbies": hobbies,
                      "learn": learn
                  })


def create_hobbie(request):
    if request.method == "POST":
        Hobbies.objects.create(
            title=request.POST['title'],
            practice_duration=request.POST['practice_duration'],
            frequency=request.POST['frequency'],
            benefits=request.POST['benefits'])
        return redirect("home")
    return render(request, "formshobbie.html", context={"action": "Adicionar"})


def update_hobbie(request, id):
    hobbie = Hobbies.objects.get(id=id)
    if request.method == "POST":
        hobbie.title = request.POST['title']
        hobbie.practice_duration = request.POST['practice_duration']
        hobbie.frequency = request.POST['frequency']
        hobbie.benefits = request.POST['benefits']
        hobbie.save()

        return redirect("home")
    return render(request,"formshobbie.html",context={"action": "Atualizar","hobbie": hobbie})


def delete_hobbie(request, id):
    hobbie = Hobbies.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            hobbie.delete()
        return redirect("home")
    return render(request, "are_you_sure.html", context={"hobbie": hobbie})


def create_learn(request):
    if request.method == "POST":
        Learn.objects.create(
            title=request.POST['title'],
            category=request.POST['category'],
            priority=request.POST['priority'],
            current_level=request.POST['current_level'],
        )
        return redirect("home")
    return render(request, "formslearn.html")


def update_learn(request, id):
    learn = Learn.objects.get(id=id)
    if request.method == "POST":
        learn.title = request.POST['title']
        learn.category = request.POST['category']
        learn.priority = request.POST['priority']
        learn.current_level = request.POST['current_level']
        learn.save()
        return redirect("home")

    return render(request,"formslearn.html",context={"action": "Atualizar","learn": learn})


def delete_learn(request, id):
    learn = Learn.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            learn.delete()
        return redirect("home")
    return render(request, "are_you_sure.html", context={"learn": learn})
