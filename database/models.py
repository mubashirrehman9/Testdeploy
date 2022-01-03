from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discription = models.TextField(max_length=200)
    discount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/upload_to", null=True, blank=True)
    trend = models.BooleanField(default=False)
    off = models.IntegerField(default=0)
    spacification = models.CharField(max_length=200, default="")
    is_slider = models.BooleanField(default=False)

    # @staticmethod
    # def get_all_brand():
    #     return Product.objects.all()
    #
    # @staticmethod
    # def get_all_brand_by_id(item_id):
    #     if item_id:
    #         return Product.objects.filter(subcategory_id=item_id)
    #     else:
    #         Product.get_all_brand()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="media", default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductDiscription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title1_image = models.ImageField(upload_to="media", default="")
    title1_heading = models.CharField(max_length=200)
    title1_discription = models.TextField()
    title2_image = models.ImageField(upload_to="media", default="")
    title2_heading = models.CharField(max_length=200)
    title2_discription = models.TextField()
    title3_image = models.ImageField(upload_to="media", default="")
    title3_heading = models.CharField(max_length=200)
    title3_discription = models.TextField()
    title4_image = models.ImageField(upload_to="media", default="")
    title4_heading = models.CharField(max_length=200)
    title4_discription = models.TextField()
    title5_image = models.ImageField(upload_to="media", default="")
    title5_heading = models.CharField(max_length=200)
    title5_discription = models.TextField()


class AditionalInform(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=300)
    Weight_Dimensions = models.TextField()
    display = models.TextField()
    iSight_Camera = models.TextField()
    VideoRecording = models.TextField()

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=160)
    verify = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    createDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.createDate)


