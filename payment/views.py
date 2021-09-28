from django.shortcuts import redirect,HttpResponse,render
from siteSettings.models import SiteSettings
from django.contrib import messages
from courses.models import Students,Courses
from carts.models import *
from zeep import Client
import datetime



def Factor_page(request):
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'فاکتور'

    cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if cart is None:
        cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)


    physical_check = cart.physical_set.filter(cart__owner_id=request.user.id, is_paid=False).all()
    digital_check = cart.digital_set.filter(cart__owner_id=request.user.id, is_paid=False).all()
    course_check = cart.courses_set.filter(cart__owner_id=request.user.id,is_paid=False).all()



    status = None
    if len(physical_check) != 0:
        status = True
    else: status = False


    if request.method == "POST":
        try:
            reciver = request.POST['reciver']
            address = request.POST['address']
            PostalCode = request.POST['PostalCode']
        except:
            cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

            if cart.total_price == 0:
                
                for c in course_check: # c = course
                    student_filter= Students.objects.filter(owner=request.user,course_id=c.course_id).first()
                    if student_filter is  None:
                        student_create = Students.objects.create(owner=request.user,course_id=c.course_id)
                    else : pass

                    course_filter = Courses.objects.filter(CourseName=c.course).first()
                    course_filter.students += 1
                    course_filter.save()
                    
                    c.is_paid = True
                    c.payment_date = datetime.datetime.now()
                    c.save()


                for d in digital_check: # p = physical
                    d.payment_date = datetime.datetime.now()
                    d.is_paid = True
                    d.save()

                        
                messages.success(request,'محصول خریداری شد')
                return redirect('userPanel:userPanel_page')

            else: return redirect('payment:request_page')



        if len(reciver) > 0:
            if len(address) > 0:
                if len(PostalCode) > 0:
                    TotalPrice = 0

                    for p in physical_check:
                        if p.price == "رایگان":
                            pass
                        else: TotalPrice += int(p.price)
                    
                    for d in digital_check:
                        if d.price == "رایگان":
                            pass
                        else: TotalPrice += int(d.price)

                    for c in course_check:
                        if c.price == "رایگان":
                            pass
                        else: TotalPrice += int(c.price)

                    if TotalPrice == 0:
                        
                        for c in course_check: # c = course
                            student_filter= Students.objects.filter(owner=request.user,course_id=c.course_id).first()
                            if student_filter is  None:
                                student_create = Students.objects.create(owner=request.user,course_id=c.course_id)
                            else : pass

                            course_filter = Courses.objects.filter(CourseName=c.course).first()
                            course_filter.students += 1
                            course_filter.save()

                            c.is_paid = True
                            c.payment_date = datetime.datetime.now()
                            c.save()

                        for p in physical_check: # p = physical
                            p.reciver = reciver
                            p.address = address
                            p.PostalCode = PostalCode
                            p.is_paid = True
                            p.payment_date = datetime.datetime.now()
                            p.save()

                        for d in digital_check: # p = physical
                            d.payment_date = datetime.datetime.now()
                            d.is_paid = True
                            d.save()

                        
                        messages.success(request,'محصول خریداری شد')
                        return redirect('userPanel:userPanel_page')
                        

                    else:

                        for p in physical_check: # p = physical
                            p.reciver = reciver
                            p.address = address
                            p.PostalCode = PostalCode
                            p.save()
                        
                        return redirect('payment:request_page')


                else: messages.error(request,'لطفا کد پستی را وارد کنید')

            else: messages.error(request,'لطفا آدرس را وارد کنید')

        else: messages.error(request,'لطفا نام و نام خانوادگی گیرنده را وارد کنید')

        
    
    cart_len = False

    if len(digital_check) == 0:
        if len(physical_check) == 0:
            if len(course_check) == 0:
                cart_len = True
            else: pass
        else: pass
    else: pass

    context = {
        "status": status,
        "cart_len": cart_len,
        "title": title,
        "TotalPrice": cart.total_price,
        "tp": cart.discountCode,
    }


    return render(request,'payment/Factor/Factor.html',context)




client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/payment/verify/'

def send_request(request):
    if not request.user.is_authenticated:
        return redirect('account:login_page')

    settings:SiteSettings = SiteSettings.objects.last()
    MERCHANT = f'{settings.toekn_zarinpal}'
    email = f'{settings.email}'
    description = f"خرید محصول از {settings.title}"
    mobile = f'{settings.phone}'
    cart = Cart.objects.filter(owner=request.user, is_paid=False).first()
    amount = f'{cart.total_price - cart.discountCode}'
    if amount == 0:
        return redirect('/')
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))





def verify(request):
    settings = SiteSettings.objects.last()
    MERCHANT = f'{settings.toekn_zarinpal}'

    if request.GET.get('Status') == 'OK':
        cart = Cart.objects.filter(owner=request.user, is_paid=False).first()
        amount = f'{cart.total_price - cart.discountCode}'
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:

            cart = Cart.objects.filter(owner=request.user, is_paid=False).first()
            cart.is_paid = True
            cart.payment_date = datetime.datetime.now()
            cart.tracking_code = result.ref_id
            cart.save()

            physical_check = cart.physical_set.filter(cart__owner_id=request.user.id, is_paid=False).all()
            digital_check = cart.digital_set.filter(cart__owner_id=request.user.id, is_paid=False).all()
            course_check = cart.courses_set.filter(cart__owner_id=request.user.id,is_paid=False).all()


            for p in physical_check:
                p.payment_date = datetime.datetime.now()
                p.is_paid = True
                p.save()

            for d in digital_check:
                d.payment_date = datetime.datetime.now()
                d.is_paid = True
                d.save()

            for c in course_check:
                student_filter= Students.objects.filter(owner=request.user,course_id=c.course_id).first()
                if student_filter is  None:
                    student_create = Students.objects.create(owner=request.user,course_id=c.course_id)
                else : pass

                course_filter = Courses.objects.filter(CourseName=c.course).first()
                course_filter.students += 1
                course_filter.save()

                c.payment_date = datetime.datetime.now()
                c.is_paid = True
                c.save()

            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')