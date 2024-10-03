from django.db import models

class Type_of_home(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default="#FFFFFF")  # حقل اللون

    def __str__(self):
        return self.title

# نموذج العنصر
class DataItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)  # العنوان
    type = models.ForeignKey(Type_of_home, on_delete=models.CASCADE)  # نوع البيانات
    place_map_1 = models.FloatField(blank=True, null=False)  # إحداثيات المكان الأول (خط العرض)
    place_map_2 = models.FloatField(blank=True, null=False)  # إحداثيات المكان الثاني (خط الطول)
    img = models.ImageField(upload_to="static/imageDataItem/%Y/%m/%d", blank=True, null=True)  # صورة

    def __str__(self):
        return self.title

# نموذج الوسائط
class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    data_item = models.ForeignKey(DataItem, related_name="media", on_delete=models.CASCADE)
    file = models.FileField(upload_to="static/media/%Y/%m/%d")  # الملفات (صور أو فيديوهات)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)

    def __str__(self):
        return f"{self.media_type.capitalize()}: {self.file.name}"

    def save(self, *args, **kwargs):
        # يمكنك إضافة عملية تخصيص هنا، مثل تصغير الصور أو التأكد
        pass
