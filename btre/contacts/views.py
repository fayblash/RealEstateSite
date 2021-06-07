from django.shortcuts import render,get_object_or_404
from listings.models import Listing


# Create your views here.
def contact(request, listing_id):
    
    listing=Listing.objects.get(id=listing_id)
    context={'listing':listing}
    return render(request,'contacts/contact.html',context)
    
    # if request.method=='POST':
    
    #     listing=request.POST['listing']
    #     listing_id=request.POST['listing_id']
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     phone=request.POST['phone']
    #     message=request.POST['message']
    #     user_id=request.POST['user_id']
    #     realtor_email=request.POST['realtor_email']
    
    #     contact=Contact(
    #         listing=listing,
    #         listing_id=listing_id,
    #         name=name,
    #         email=email,
    #         phone=phone,
    #         message=message,
    #         user_id=user_id
    #     )
    #     send_mail(
    #         'Property Listing Inquiry',
    #         'There has been an inquiry for' + listing + '.Sign into the admin panel for more info.',
    #         'traversy.brad@gmail.com',
    #         [realtor_email,'techguiinfo@gmail.com'],
    #         fail_silently=False
    #     )
        
    #     contact.save()
        
    # return redirect('/listings/'+listing_id)