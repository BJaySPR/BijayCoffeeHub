from django.shortcuts import render

# Create your views here.

class Home():
    def home(request):
        return render(request, 'main/index.html')
    
class About():
    def about(request):
        return render(request, 'main/about.html')
    
class Contact():
    def contact(request):
        return render(request, 'main/contact.html')

class Menu():
    def menu(request):
        return render(request, 'main/menu.html')
    
class Reservation():
    def reservation(request):
        return render(request, 'main/reservation.html')
    
class Service():
    def service(request):
        return render(request, 'main/service.html')

class Testimonial():
    def testimonial(request):
        return render( request, 'main/testimonial.html')