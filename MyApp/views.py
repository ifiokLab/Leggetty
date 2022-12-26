from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'MyApp/index.html')

def About(request):
    return render(request,'MyApp/about-us.html')


def Calculate_Cost(request):
    return render(request,'MyApp/calculate-cost.html')


def College_Funding(request):
    return render(request,'MyApp/College-Funding.html')


def Financial_Aid(request):
    return render(request,'MyApp/Financial-Aid.html')


def Financial_Strategies(request):
    return render(request,'MyApp/Financial-Strategies.html')


def Free_Money(request):
    return render(request,'MyApp/Free-Money.html')


def funding_secret(request):
    return render(request,'MyApp/funding-secret.html')


def loan_secret(request):
    return render(request,'MyApp/loan-secret.html')



def Maximize_money(request):
    return render(request,'MyApp/Maximize-money.html')

def Private_Clients(request):
    return render(request,'MyApp/Private-Clients.html')


def Reduce_loans(request):
    return render(request,'MyApp/Reduce-loans.html')



def retirement_restoration(request):
    return render(request,'MyApp/retirement-restoration.html')

def school_Scholarships(request):
    return render(request,'MyApp/school-Scholarships.html')


def services(request):
    return render(request,'MyApp/services.html')


def training_video(request):
    return render(request,'MyApp/training-video.html')


def Live_Workshop(request):
    return render(request,'MyApp/live-workshop.html')


def processes(request):
    return render(request,'MyApp/process.html')

def Testimonials(request):
    return render(request,'MyApp/testimonials.html')


def Resources(request):
    return render(request,'MyApp/resources.html')


def Video_Testimonials(request):
    return render(request,'MyApp/video-testimonial.html')