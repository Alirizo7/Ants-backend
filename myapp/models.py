from django.db import models




class PhoneName(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    






class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField()
    size = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=50)
    about = models.TextField()
    cost = models.IntegerField()




    def __str__(self):
        return self.title
    



# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     about = models.ForeignKey(About, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    

