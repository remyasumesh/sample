from django.shortcuts import render
from decimal import Decimal


# Create your views here.
def HomePage(request):
    return render(request,'HomePage.html')

# def sum(request):
#     if request.method == 'POST':
#         num1 = int(request.POST['number1'])
#         num2 = int(request.POST['number2'])

#         result = num1 + num2

#         return render(request, 'result.html', {'r': result})


def sum(request):
    if request.method == 'POST' :
        number1=request.POST.get('number1','',)
        number2=request.POST.get('number2','',)

        if not number1 or not number2 :
            return render (request,'error.html')
        
        num1=Decimal(number1)
        num2=Decimal(number2)
        result=num1+num2
        return render(request,'result.html',{'r': result})
    
    else:
        return render (request,'error.html')
