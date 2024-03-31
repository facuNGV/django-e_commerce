from django.db import models


from django.contrib.auth.models import User


class Comic(models.Model):

    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel id', null=False, blank=False, unique=True
    )
    title = models.CharField(
        verbose_name='title', max_length=120, default=''
    )
    description = models.TextField(verbose_name='description', default='')
    price = models.FloatField(
        verbose_name='price', max_length=5, default=0.00
    )
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0
    )
    picture = models.URLField(verbose_name='picture', default='')

    class Meta:
        db_table = 'e_commerce_comics'
        verbose_name = 'comic'
        verbose_name_plural = 'comics'

    def __str__(self):
        return f'{self.id} - {self.title}'


class WishList(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name='user',
        on_delete=models.CASCADE,
        default=1,
        blank=True
    )
    comic = models.ForeignKey(
        Comic,
        verbose_name='comic',
        on_delete=models.CASCADE,
        default=1,
        blank=True
    )
    favorite = models.BooleanField(verbose_name='favorite', default=False)
    cart = models.BooleanField(verbose_name='cart', default=False)
    wished_qty = models.PositiveIntegerField(
        verbose_name='wished qty', default=0
    )
    bought_qty = models.PositiveIntegerField(
        verbose_name='bought qty', default=0
    )

    class Meta:
        db_table = 'e_commerce_wish_list'
        verbose_name = 'wish list'
        verbose_name_plural = 'wish lists'

    def __str__(self):
        return f'{self.id}'

