from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bids(models.Model):
    price = models.FloatField(default=0)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

    def __str__(self):
        return f"{self.price}"

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.CharField(max_length= 1000)
    bid = models.ForeignKey(Bids, on_delete=models.CASCADE, blank=True, null=True, related_name="bids")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="categories")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userList")
    create_time = models.DateTimeField(auto_now_add=True)
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="watchlist")

    is_Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing_comment = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} comment on {self.listing_comment}"