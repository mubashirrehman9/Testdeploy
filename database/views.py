from django.views.generic import TemplateView

from .task import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
import uuid
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, get_user_model
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import UserReg, ContactForm, FirstloginForm, ChangeForm, NewpasswordForm, EditUserProfileform, RatingForm
from .models import Product, Category, Contact, Profile, Review, Subcategory, AditionalInform, ProductDiscription, \
    ProductImage

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views
from django.contrib.auth.decorators import login_required


# @login_required(login_url="/login/")
# def index(request):
#     mobile_products = Product.objects.filter(category__name="Mobile")[:6]
#     products = Product.objects.filter(trend=True)[:6]
#     tablet_products = Product.objects.filter(category__name="Tablet")
#     mobile_subcategory = Subcategory.objects.filter(category__name="Mobile")[:6]
#     laptop_subcategory = Subcategory.objects.filter(category__name="Laptop")
#     tablet_subcategory = Subcategory.objects.filter(category__name="Tablet")
#     is_slider = Product.objects.filter(is_slider=True)
#     is_promotion = Product.objects.filter(is_slider=True)[:4]
#     category = Category.objects.all()
#     categories = Subcategory.objects.all()
#     item_id = request.GET.get('item')
#     context = {
#         'mobile_products': mobile_products,
#         'msubcategory': mobile_subcategory,
#         'lsubcategory': laptop_subcategory,
#         'tsubcategory': tablet_subcategory,
#         'products': products,
#         'tablet_products': tablet_products,
#         'categories': categories,
#         'item_id': item_id,
#         'category': category,
#         'is_slider': is_slider,
#         'is_promotion': is_promotion,
#     }
#     return render(request, 'database/index.html', context)
class index(TemplateView):
    template_name = 'database/index.html'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        mobile_products = Product.objects.filter(category__name="Mobile")[:6]
        products = Product.objects.filter(trend=True)[:6]
        tablet_products = Product.objects.filter(category__name="Tablet")
        mobile_subcategory = Subcategory.objects.filter(category__name="Mobile")[:6]
        laptop_subcategory = Subcategory.objects.filter(category__name="Laptop")
        tablet_subcategory = Subcategory.objects.filter(category__name="Tablet")
        is_slider = Product.objects.filter(is_slider=True)
        is_promotion = Product.objects.filter(is_slider=True)[:4]
        category = Category.objects.all()
        categories = Subcategory.objects.all()
        # item_id = request.GET.get('item')
        context = {
            'mobile_products': mobile_products,
            'msubcategory': mobile_subcategory,
            'lsubcategory': laptop_subcategory,
            'tsubcategory': tablet_subcategory,
            'products': products,
            'tablet_products': tablet_products,
            'categories': categories,
            # 'item_id': item_id,
            'category': category,
            'is_slider': is_slider,
            'is_promotion': is_promotion,
        }
        return context


# def index1(request, id):
#     mproduct = Product.objects.filter(subcategory=id).filter(category__name="Mobile")[:5]
#
#     context = {
#         'mobile_products': mproduct,
#
#     }
#     return render(request, 'database/filter.html', context)
class index1(TemplateView):
    template_name = 'database/filter.html'

    def get_context_data(self, *args, **kwargs):
        mproduct = Product.objects.filter(subcategory=self.kwargs['id']).filter(category__name="Mobile")[:5]

        context = {
            'mobile_products': mproduct,

        }
        return context


# def index2(request, id):
#     tproduct = Product.objects.filter(subcategory=id).filter(category__name="Tablet")[:5]
#
#     context = {
#
#         'tab_products': tproduct,
#
#     }
#     return render(request, 'database/filter1.html', context)
class index2(TemplateView):
    template_name = 'database/filter1.html'

    def get_context_data(self, *args, **kwargs):
        tproduct = Product.objects.filter(subcategory=self.kwargs['id']).filter(category__name="Tablet")[:5]

        context = {

            'tab_products': tproduct,

        }
        return context


class index4(TemplateView):
    template_name = 'database/filter4.html'

    def get_context_data(self, *args, **kwargs):
        tproduct = Product.objects.filter(category=self.kwargs['id'])[:5]

        context = {

            'products': tproduct,

        }
        return context


# def product_detail(request, id):
#     product = Product.objects.filter(trend=True)[:6]
#     product_det = Product.objects.get(id=id)
#     pro_images = ProductImage.objects.filter(id=id)
#     review_data = Review.objects.filter(product_id=id).order_by('-createDate')
#     # pro_description = ProductDiscription.objects.all()
#     pro_det_description = ProductDiscription.objects.filter(product=id)
#     prod_aditional_infrm = AditionalInform.objects.filter(product=id)
#     if request.method == 'POST':
#
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.user.is_authenticated:
#                 form.user = request.user
#                 form.product = product_det
#                 pro = request.POST.get('prod_id')
#                 form.rating = pro
#                 form.save()
#             else:
#                 return redirect("login")
#     form = RatingForm()
#     context = {'pro_descriptions': pro_det_description, 'product_det': product_det, "pro_images": pro_images,
#                'prod_aditionanl_infrm': prod_aditional_infrm,
#                'product': product, 'review_data': review_data, 'form': form,
#                }
#     return render(request, 'database/product_detail.html', context)
class product_detail(TemplateView):
    template_name = 'database/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        product = Product.objects.filter(trend=True)[:6]
        product_det = Product.objects.get(id=self.kwargs['id'])
        pro_images = ProductImage.objects.filter(id=self.kwargs['id'])
        review_data = Review.objects.filter(product_id=self.kwargs['id']).order_by('-createDate')
        pro_det_description = ProductDiscription.objects.filter(product=self.kwargs['id'])
        prod_aditional_infrm = AditionalInform.objects.filter(product=self.kwargs['id'])
        form = RatingForm()
        context = {'pro_descriptions': pro_det_description, 'product_det': product_det, "pro_images": pro_images,
                   'prod_aditionanl_infrm': prod_aditional_infrm,
                   'product': product, 'review_data': review_data, 'form': form
                   }
        return  context

    def post(self, request, id):
        product_det = Product.objects.get(id=id)
        form = RatingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.user = request.user
                form.product = product_det
                pro = request.POST.get('prod_id')
                form.rating = pro
                form.save()
            else:
                return redirect("login")
            form = RatingForm()
            context = {'form': form,
                       }
            return render(request, 'database/product_detail.html', context)


#
#
# def index3(request):
#     product1 = Product.objects.all()
#     keyword = request.GET.get('keyword')
#     price_min = request.GET.get('price_min')
#     price_max = request.GET.get('price_max')
#     if keyword is not None:
#         product1 = Product.objects.filter(name__icontains=keyword,
#                                           price__range=[price_min, price_max])
#
#     return render(request, 'database/filter3.html', {'product': product1})


class index3(View):
    def get(self, request):
        product1 = Product.objects.all()
        keyword = request.GET.get('keyword')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        if keyword is not None:
            product1 = Product.objects.filter(name__icontains=keyword)
        if price_min and price_max is not None:
            product1 = Product.objects.filter(price__range=[price_min, price_max])
            # if price_max or price_min is None:
            #     product1 = Product.objects.filter(name__icontains=keyword)
        return render(request, 'database/filter3.html', {'product': product1})


# def product(request):
#     product = Product.objects.all()
#     category = Category.objects.all()
#     keyword = request.GET.get('keyword')
#     price_min = request.GET.get('price_min')
#     price_max = request.GET.get('price_max')
#     if keyword is not None:
#         product = Product.objects.filter(name__icontains=keyword, price__range=[price_min, price_max])
#
#     context = {
#         'category': category,
#         'product': product,
#
#     }
#     return render(request, 'database/product.html', context)
class product(View):
    def get(self, request):
        product = Product.objects.all()
        category = Category.objects.all()
        keyword = request.GET.get('keyword')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        if keyword is not None:
            product = Product.objects.filter(name__icontains=keyword, price__range=[price_min, price_max])

        context = {
            'category': category,
            'product': product,

        }
        return render(request, 'database/product.html', context)


# def about(request):
#     return render(request, 'database/about_us.html')

class about(View):

    def get(self, request):
        return render(request, 'database/about_us.html')


#
# def detail(request, id):
#     if request.method == 'GET':
#         getid = Product.objects.get(id=id)
#         # obj = Review.objects.filter(rating=0).or
#         data = Review.objects.filter(product=getid)
#         fm = RatingForm()
#         return render(request, 'database/product_detail.html', {'product': getid, 'form': fm, 'data': data})
#     if request.method == 'POST':
#         getid = Product.objects.get(id=id)
#         data = Review.objects.filter(product=getid)
#         review_data = Review.objects.filter(product_id=id).order_by('-created_at')
#         fm = RatingForm(request.POST)
#
#         if fm.is_valid():
#             profile = fm.save(commit=False)
#             profile.user = request.user
#             profile.product = getid
#             profile.save()
#
#             # fm.save()
#         #
#         return render(request, 'database/product_detail.html', {'product': getid, 'form': fm, 'data': data})


# def detail(request, id):
#     product_det = Product.objects.get(id=id)
#
#     review_data = Review.objects.filter(product_id=id).order_by('-createDate')
#
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         rating = request.POST['prod_id']
#         print(rating)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.user.is_authenticated:
#                 form.user = request.user
#                 form.product = product_det
#                 form.rating = rating
#                 form.save()
#
#
#             else:
#                 return redirect("login")
#     form = RatingForm()
#     context = {'product_det': product_det,
#                'product': product, 'review_data': review_data,
#                'form': form,
#                }
#     return render(request, 'database/product_detail.html', context)


def search(request):
    return render(request, 'database/search_results.html')


def account(request):
    return render(request, 'database/my_account.html')


def checkout(request):
    return render(request, 'database/checkout_payment.html')


def checkout_info(request):
    return render(request, 'database/checkout_info.html')


def checkout_complete(request):
    return render(request, 'database/checkout_complete.html')


def checkout_cart(request):
    return render(request, 'database/checkout_cart.html')


def faq(request):
    return render(request, 'database/faq.html')


# registration form


class MyRegister(View):

    def post(self, request):
        fm = UserReg(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).first():
            messages.success(request, ' Already email exist .')
            return redirect('registration1')
        if not User.objects.filter(email=email).first():
            messages.success(request, 'Please check in your gmail for verify .')
            if fm.is_valid():
                new_user = fm.save()
                uid = uuid.uuid4()
                profile_obj = Profile(user=new_user, token=uid)
                profile_obj.save()
                send_mail_task(new_user.email, uid)
                # send_mail_task.delay(new_user.email, uid)
                return redirect('registration1')
        else:
            return render(request, 'database/regis.html', {'form': fm})

    def get(self, request):
        fm = UserReg()
        return render(request, 'database/regis.html', {'form': fm})


#
def send_mail_after_registration(email, token):
    subject = 'change password'
    message = f'Please click on the given link to change your password http://127.0.0.1:8000/registration/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, token):
    profile_obj = Profile.objects.filter(token=token).first()
    if profile_obj.verify == False:
        profile_obj.verify = True
        profile_obj.save()
        messages.success(request, "Your email has been successfully verified")
        return redirect('loginform')
    if profile_obj.verify == True:
        messages.success(request, "Your email has been Already verified")
        return redirect('loginform')


class MyContact(View):
    def post(self, request):
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('contact_us')

    def get(self, request):
        fm = ContactForm(label_suffix=':')
        return render(request, 'database/contact_us.html', {'form': fm})


class Loginform(View):
    def post(self, request):
        fm = FirstloginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user_obj = User.objects.filter(username=uname).first()
            if user_obj is None:
                messages.success(request, 'user is not found')
                return redirect('loginform')
            profile_obj = Profile.objects.filter(user=user_obj).first()
            if not profile_obj.verify:
                messages.success(request, 'email not verify')
                return redirect('loginform')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/index')

        return render(request, 'database/login.html', {'form': fm})

    def get(self, request):
        fm = FirstloginForm()
        return render(request, 'database/login.html', {'form': fm})


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('index')


class Changepassword(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = ChangeForm(user=request.user)
            return render(request, 'database/changepassword.html', {'form': fm})

        else:
            return HttpResponseRedirect('login')

    def post(self, request):

        fm = ChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'password change success!')
        return HttpResponseRedirect('index')


class Newpassword(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = NewpasswordForm(user=request.user)
            return render(request, 'database/changepassword.html', {'form': fm})

        else:
            return HttpResponseRedirect('login')

    def post(self, request):

        fm = NewpasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'password change success!')
        return HttpResponseRedirect('index')


class Changeprofile(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = EditUserProfileform(instance=request.user)
            return render(request, 'database/changeover.html', {'form': fm})

        else:
            return HttpResponseRedirect('login')

    def post(self, request):
        fm = EditUserProfileform(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()

        return HttpResponseRedirect('index')
