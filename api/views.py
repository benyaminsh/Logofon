from rest_framework.response import Response
from discountCode.models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from carts.models import *
import datetime




@api_view(['POST'])
def addOrder(request):
    try:
        product_id = request.POST['id']

        cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

        if cart is None:
            cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)
        else: pass

        product = Product.objects.filter(id=product_id).first()


        physical_check = cart.physical_set.filter(product_id=product_id).first()
        digital_check = cart.digital_set.filter(product_id=product_id).first()


        if physical_check is not None or digital_check is not None:
            return Response({'status': 'False'},status=status.HTTP_204_NO_CONTENT)


        else:
            if product.price == 0:
                product.price = 'رایگان'
            else: pass

            if product.digital_or_physical == True:
                cart.physical_set.create(product_id=product.id, price=product.price,slug=product.slug)

                if product.price != 'رایگان':
                    if cart.total_price == 0:
                        cart.total_price = int(product.price)
                        cart.save()
                    else:
                        cart.total_price += int(product.price)
                        cart.save()
                else: pass

                return Response({'status': 'True'}, status=status.HTTP_200_OK)
            else:
                cart.digital_set.create(product_id=product.id, price=product.price,slug=product.slug)

                if product.price != 'رایگان':
                    if cart.total_price == 0:
                        cart.total_price = int(product.price)
                        cart.save()
                    else:
                        cart.total_price += int(product.price)
                        cart.save()
                else: pass

                return Response({'status': 'True'}, status=status.HTTP_200_OK)



    except: return Response({'status': 'Error'},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def deleteOrder(request):
    try:
        id = request.POST['id']


        cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

        if cart is None:
            cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)


        physical_check = cart.physical_set.filter(id=id).first()
        digital_check = cart.digital_set.filter(id=id).first()


        if physical_check is None and digital_check is None:
            return Response({'status': 'False'},status=status.HTTP_204_NO_CONTENT)

        else:

            if physical_check is not None:
                if physical_check.price != 'رایگان':
                    cart.total_price -= int(physical_check.price)
                    cart.save()
                else: pass
                physical_check.delete()
                return Response({'status': 'True'}, status=status.HTTP_200_OK)

            else:
                if digital_check.price != 'رایگان':
                    cart.total_price -= int(digital_check.price)
                    cart.save()
                else: pass
                digital_check.delete()
                return Response({'status': 'True'}, status=status.HTTP_200_OK)



    except: return Response({'status': 'Error'},status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def addCourses(request):
    try:

        id = request.POST['id']

        cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

        if cart is None:
            cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)
        else:
            pass

        course_check = cart.courses_set.filter(course_id=id).first()

        if course_check is not None:
            return Response({'status': 'False'}, status=status.HTTP_204_NO_CONTENT)

        else:
            course = Courses.objects.filter(id=id).first()
            if course.CoursePrice == 0:
                course.CoursePrice = 'رایگان'
            else: pass

            cart.courses_set.create(price=course.CoursePrice, course_id=id,slug=course.CourseSlug)
            if course.CoursePrice != 'رایگان':
                if cart.total_price == 0:
                    cart.total_price = course.CoursePrice
                    cart.save()
                else:
                    cart.total_price += course.CoursePrice
                    cart.save()
            else: pass
            return Response({'status': 'True'}, status=status.HTTP_200_OK)

    except: return Response({'status': 'Error'}, status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def deleteCourses(request):
    try:

        id = request.POST['id']
   

        cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

        if cart is None:
            cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)
        else:
            pass

        course = cart.courses_set.filter(id=id).first()


        if course is None:
            return Response({'status': 'False'}, status=status.HTTP_204_NO_CONTENT)

        else:
            if course.price != 'رایگان':
                cart.total_price -= int(course.price)
                cart.save()
            else: pass
            course.delete()
            return Response({'status': 'True'}, status=status.HTTP_200_OK)

    except: return Response({'status': 'Error'}, status=status.HTTP_404_NOT_FOUND)



@api_view()
def number(request):
    try:

        cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

        if cart is None:
            cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)


        physical_check = cart.physical_set.filter(cart__owner_id=request.user.id,is_paid=False).first()
        digital_check = cart.digital_set.filter(cart__owner_id=request.user.id,is_paid=False).first()
        course_check = cart.courses_set.filter(cart__owner_id=request.user.id,is_paid=False).first()

        if physical_check is None and digital_check is None and course_check is None:
            return Response({'Number': '0'})
        else:
            physical = cart.physical_set.filter(cart__owner_id=request.user.id,is_paid=False).count()
            digital = cart.digital_set.filter(cart__owner_id=request.user.id,is_paid=False).count()
            course = cart.courses_set.filter(cart__owner_id=request.user.id, is_paid=False).count()
            number = physical + digital + course
            return Response({'Number': number,},status=status.HTTP_200_OK)

    except: return Response({'status': 'Error'},status=status.HTTP_404_NOT_FOUND)


@api_view()
def list(request):
    cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if cart is None:
        cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)

    physical_check = cart.physical_set.filter(cart__owner_id=request.user.id, is_paid=False).all() # pl
    digital_check = cart.digital_set.filter(cart__owner_id=request.user.id, is_paid=False).all() # dg
    course_check = cart.courses_set.filter(cart__owner_id=request.user.id,is_paid=False).all() # ce

   
    List = []

    
    for pl in physical_check:
        List.append({'id': pl.id,'slug': pl.slug,'title': pl.product.title,'price': pl.product.price,'photo': pl.product.image.url})

    for dg in digital_check:
        List.append({'id': dg.id,'slug': dg.slug,'title': dg.product.title,'price': dg.product.price,'photo': dg.product.image.url})

    for ce in course_check:
        List.append({'id': ce.id,'slug': ce.slug,'title': ce.course.CourseName,'price': ce.course.CoursePrice,'photo': ce.course.CourseImage.url})


    return JsonResponse(List,safe=False)


@api_view(["POST"])
def discountCode(request):

    cart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if cart is None:
        cart = Cart.objects.create(owner_id=request.user.id, is_paid=False)

    
    code = request.POST['code']


    discountCode = DiscountCode.objects.filter(code=code).first()

    if discountCode is None:
        return Response({'Error': "کد تخفیف منقضی شده است یا وجود ندارد"},status=status.HTTP_510_NOT_EXTENDED)
    
    else:

        users_discountCode = Users_DiscountCode.objects.filter(user_id=request.user.id,code=code).first()

        if users_discountCode is not None:
            print('استفاده شده')
            return Response({'Error': "کد تخفیف استفاده شده است "},status=status.HTTP_510_NOT_EXTENDED)
        else:

            TotalPrice = cart.total_price - discountCode.discount_percent

            if TotalPrice <= 0:
                return Response({'Error': "کد تخفیف اعمال نمیشود"},status=status.HTTP_510_NOT_EXTENDED)
            else:
                cart.discountCode = discountCode.discount_percent
                cart.save()
                discountCode.users += 1
                discountCode.save()
                users_discountCode = Users_DiscountCode.objects.create(user_id=request.user.id,code=code,discount_percent=discountCode.discount_percent)
                return Response({'Ok': "کد تخفیف اعمال شد",'ToTalPrice': discountCode.discount_percent,},status=status.HTTP_200_OK)



 