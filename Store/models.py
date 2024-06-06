from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Tag (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    author = models.CharField(max_length=100 ,null=True, blank=True)
    price = models.CharField(max_length=100 ,null=True)
    issuDate = models.DateField(null=True, blank=True)
    CATOGRTY = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Biography', 'Biography'),
        ('Thriller', 'Thriller'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Mystery', 'Mystery'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Self-Help', 'Self-Help'),
        ('Health', 'Health'),
        ('Cooking', 'Cooking'),
        ('History', 'History'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Business', 'Business'),
        ('Politics', 'Politics'),
        ('Religion', 'Religion'),
        ('Spirituality', 'Spirituality'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),

    ]
    category = models.CharField(max_length=100, choices=CATOGRTY)
    tag = models.ManyToManyField(Tag, blank=True, null= True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    STATUS = [
       ('IN ORDER','IN ORDER'),
        ('DELIVERED','DELIVERED'),
        ('CANCELLED','CANCELLED'),
        ('RETURNED','RETURNED'),
        ('PENDING','PENDING'),
        ('DELIVERING','DELIVERING'),

    ]
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.customer.name