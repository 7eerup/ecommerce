from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    

class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    
    # 제품 이름 저장 최대 250자 입력 허용
    title = models.CharField(max_length=250)

    # default='un-branded': 입력되지 않으면 자동으로 'un-branded'로 저장
    brand = models.CharField(max_length=250, default='un-branded')

    #TextField: 긴 텍스트 저장 blank=True: 입력하지 않아도 유효하게 저장
    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    # max_digits=4: 전체 자릿수 (정수 + 소수점 포함) 최대 4자리 decimal_places=2: 소수점 이하 자릿수는 2자리 (예: 19.99)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    # upload_to='images/': 업로드한 이미지 파일은 /media/images/ 폴더에 저장됩니다 (MEDIA 설정 필요)
    image = models.ImageField(upload_to='images/')


    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])