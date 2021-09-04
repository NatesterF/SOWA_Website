from django.shortcuts import render
from django.http import *
from .forms import MealForm
from .models import *

# Create your views here.
def form(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        meallog=form.save(commit=False)
        meallog.save()
        if form.is_valid():
            return HttpResponseRedirect('./thanks/')
    else:
        form = MealForm()

    return render(request,"logging/form.html",{'form': form})

def formSubmitted(request):
        return render(request,"logging/thanks.html")
def getLeaderboard(request):
        leaderboard= LeaderboardModel.objects.raw("SELECT 1 id, group_name,count(*) as meals_eaten FROM log_meals_meallog GROUP BY group_name ORDER BY count(*) desc")
        for item in leaderboard:
            print(item.group_name)
        return render(request,"logging/leaderboard.html",{'leaderboard': leaderboard})
