from django.shortcuts import render, redirect
from .models import DataItem, Media, Type_of_home  # استيراد Type_of_home
from .forms import DataItemForm, MediaFormSet
import json

# الصفحة الرئيسية لعرض البيانات
def index(request):
    dataitems = DataItem.objects.all().prefetch_related("media")
    dataitems_json = [
        {
            "id": item.id,
            "title": item.title,
            "type": item.type,
            "place_map_1": item.place_map_1,
            "place_map_2": item.place_map_2,
            "img": item.img.url if item.img else "",  # تحويل الصورة إلى رابط URL
            "media": [
                {
                    "media_type": media.media_type,
                    "file": media.file.url if media.file else "",  # تحويل حقل الملف إلى URL
                }
                for media in item.media.all()
            ],
        }
        for item in dataitems
    ]
    return render(request, "index.html", {"dataitems_json": json.dumps(dataitems_json)})

# صفحة لإضافة العلامات
def add_tag(request):
    if request.method == "POST":
        data_item_form = DataItemForm(request.POST, request.FILES)
        media_formset = MediaFormSet(request.POST, request.FILES)
        
        # معالجة إدخال نوع جديد
        new_type_title = request.POST.get('new_type')
        if new_type_title:
            new_type = Type_of_home.objects.create(title=new_type_title)

        if data_item_form.is_valid() and media_formset.is_valid():
            # حفظ بيانات DataItem
            data_item = data_item_form.save(commit=False)
            if new_type_title:
                data_item.type = new_type  # استخدم النوع الجديد
            data_item.save()  # احفظ العنصر بعد تعيين النوع

            # حفظ جميع الوسائط
            for form in media_formset:
                if form.cleaned_data and form.cleaned_data.get("file"):
                    media = form.save(commit=False)
                    media.data_item = data_item
                    media.save()
            return redirect("index")  # إعادة التوجيه إلى الصفحة الرئيسية بعد الإضافة
    else:
        data_item_form = DataItemForm()
        media_formset = MediaFormSet()  # فارغة عند تحميل الصفحة

    types_of_home = Type_of_home.objects.all()  # احصل على جميع الأنواع

    return render(
        request,
        "add_tag.html",
        {
            "data_item_form": data_item_form,
            "media_formset": media_formset,
            "types_of_home": types_of_home,  # تمرير الأنواع إلى القالب
        },
    )
