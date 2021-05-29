# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from .views import checkSpam, makeFilter
# from django.conf import settings
# import os
# from django.http import HttpResponse
# from .models import Contribution, Dataset, Test


# @receiver(pre_save, sender=Dataset)
# def create_filter(sender, instance, created, *args, **kwargs):
#     if created:
#         makeFilter(column=1, path=os.path.join(settings.BASE_DIR, 'datasets/storage/filter.npy'))

# def user_contribution_counter(instance):
#     print("hello there")
#     instance.contribution.sender.contributions.add(instance.contribution)
#     print(instance.contribution)
#     xp = instance.contribution.sender.xp
#     xp += 10

# def contri(sender, instance, *args, **kwargs):
#     print("sexy sex sextime")
#     spam = checkSpam(os.path.join(settings.BASE_DIR, 'datasets/storage/filter.npy'), instance.contribution.textinput)
#     if (spam):
#         instance.contribution.isSpam = True
#         print("penis very large")
#         return HttpResponse("yayy it doesnt work")
#     else:
#         print("penis very small")
#         instance.contribution.save()
#         user_contribution_counter(instance)

# pre_save.connect(contri, sender=Contribution)

# # @receiver(pre_save, sender=Test)
# # def save_test(sender, instance, **kwargs):
# #     print("my ass")

# # pre_save.connect(save_test, sender=Test)