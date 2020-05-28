from django.db import models

# Create your models here.
class Laptop(models.Model):
    CATEGORY = (
        ('Gaming', 'Gaming'),
        ('Ultrabook', 'Ultrabook'),
        ('Home/Business', 'Home/Business'),
        ('Design', 'Design')
    )

    TOUCHSCREEN = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    BACKLIGHT = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    KEYBOARD_SIZE = (
        ('TKL Keyboard - TenKeyLess', 'TKL Keyboard - TenKeyLess'),
        ('Full-size Keyboard', 'Full-size Keyboard')
    )

    category = models.CharField(max_length=32, choices=CATEGORY)
    brand = models.CharField(max_length=64)
    item_name = models.CharField(max_length=256)
    color = models.CharField(max_length=64)
    os = models.CharField(max_length=32)
    cpu = models.CharField(max_length=64)
    cpu_count = models.IntegerField()
    cpu_speed = models.CharField(max_length=32)
    gpu = models.CharField(max_length=128)
    ram_type = models.CharField(max_length=64)
    ram_size = models.CharField(max_length=64)
    screen_size = models.CharField(max_length=64)
    touchscreen = models.CharField(max_length=3, choices=TOUCHSCREEN)
    resolution = models.CharField(max_length=64)
    diskdrive = models.CharField(max_length=64)
    keyboard = models.CharField(max_length=64, choices=KEYBOARD_SIZE)
    backlight = models.CharField(max_length=3, choices=BACKLIGHT)
    backlight_color = models.CharField(max_length=32)
    ports = models.CharField(max_length=512)
    battery = models.CharField(max_length=64)
    weight = models.FloatField()
    dimension = models.CharField(max_length=64)