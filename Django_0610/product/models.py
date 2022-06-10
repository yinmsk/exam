from django.db import models

# Create your models here.

# 상품의 카테고리 이름, 카테고리 등의 정보
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(on_delete=models.CASCADE, null=False)
    explanation = models.CharField(max_length=500, on_delete=models.CASCADE, null=False)
    price = models.CharField(max_length=50, on_delete=models.CASCADE, null=False)
    Stock = models.CharField(max_length=1000, on_delete=models.CASCADE, null=False)


# 상품의 카테고리 이름이 들어가는 모델
class Category(models.Model):
    category = models.CharField(Product, max_length=50)

# 주문한 상태 저장
class OrderStatus(models.Model):
    Order = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    cancellation = models.CharField(max_length=50)
    d_start = models.CharField(max_length=50)
    d_completion = models.CharField(max_length=50)

# 7. 유저가 주문한 상품의 개수를 저장하는 ProductOrder 하는 모델을 만들어 보세요.
class ProductOrder(models.Model):
    save_order = models.CharField(max_length=50)

# 유저의 주문(주소, 가격, 할인율등) 정보를 저장 하는 곳
class UserOrder(models.Model):
    address = models.CharField(max_length=50)
    order_time = models.CharField(max_length=50)
    sale = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    boolean = models.CharField(max_length=50)
