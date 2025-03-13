from django.shortcuts import render
from .models import Count
from django.db.models import F

def counterpage(request):
    countObj = Count.objects.first()
    if(countObj == None):
        countObj = Count(count=1)
    else:
        countObj.count = F('count') + 1
    countObj.save()
    del countObj.count
    context = {'count': countObj.count}
    return render(request, "counts/index.html", context)
    
