from django.shortcuts import render
from BCH_Admin.models import our_story,our_vision
from BCH_Admin.models import HotCoffee,ColdCoffee

# Create your views here.

class Home():
    def home(request):
        hotCoffee =HotCoffee.objects.all()
        coldCoffee = ColdCoffee.objects.all()

        vision = our_vision.objects.all()
        story = our_story.objects.all
        context = {
            'vision': vision,
            'story':story,
            'hotCoffee':hotCoffee,
            'coldCoffee':coldCoffee
        }

        return render(request, 'main/index.html',context)
    
class About():

    def about(request):
        return render(request, 'main/about.html')
    
class Contact():
    def contact(request):
        return render(request, 'main/contact.html')

class Menu():
    def menu(request):
        products =HotCoffee.objects.all()
        products1 = ColdCoffee.objects.all()
          
        return render(request, 'main/menu.html',{'products':products,'products1':products1})
    
class Reservation():
    def reservation(request):
        return render(request, 'main/reservation.html')
    
class Service():
    def service(request):
        return render(request, 'main/service.html')

class Testimonial():
    def testimonial(request):
        return render( request, 'main/testimonial.html')