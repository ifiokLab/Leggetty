from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('About/',views.About,name = 'About'),
    path('Calculate_Cost/',views.Calculate_Cost,name = 'Calculate_Cost'),
    path('College_Funding/',views.College_Funding,name = 'College_Funding'),
    path('Financial_Aid/',views.Financial_Aid,name = 'Financial_Aid'),
    path('Financial_Strategies/',views.Financial_Strategies,name = 'Financial_Strategies'),
    path('Free_Money/',views.Free_Money,name = 'Free_Money'),
    path('loan_secret/',views.loan_secret,name = 'loan_secret'),
    path('Maximize_money/',views.Maximize_money,name = 'Maximize_money'),
    path('Private_Clients/',views.Private_Clients,name = 'Private_Clients'),
    path('Reduce_loans/',views.Reduce_loans,name = 'Reduce_loans'),
    path('services/',views.services,name = 'services'),
    path('retirement_restorations/',views.retirement_restoration,name = 'retirement_restoration'),
    path('training_video/',views.training_video,name = 'training_video'),
    path('Live_Workshop/',views.Live_Workshop,name = 'Live_Workshop'),

    path('Testimonials/',views.Testimonials,name = 'Testimonials'),
    path('Resources/',views.Resources,name = 'Resources'),
    path('process/',views.processes,name = 'process'),
    path('Video_Testimonials/',views.Video_Testimonials,name = 'Video_Testimonials'),
    path('school_Scholarships/',views.school_Scholarships,name = 'school_Scholarships'),



]
