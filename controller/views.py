from django.views import generic

from .models import *


class IndexView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.get(id=1)
        context['services'] = ServicesModel.objects.all()
        context['consultants'] = ConsultantsModel.objects.all()[:4]
        context['blog'] = BlogModel.objects.all()[:3]
        return context

    template_name = 'controller/index.html'

# model = BannerModel, ServicesModel
# context_object_name = 'list'
#
# object = BannerModel.objects.get(id=1)
# print(object.banner_title)
# template_name = 'controller/index.html'

# context = super(IndexView, self).get_context_data(**kwargs)
# context['key'] = 'test'
# return context
