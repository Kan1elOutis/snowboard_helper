from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from resumes.forms import ResumeCreatingForm
from resumes.models import Resume, RidingStyle


class RidingStyleListView(TitleMixin, ListView):
    model = Resume
    template_name = 'resumes/resumes.html'
    paginate_by = 3
    title = 'SibDoski - Резюме'

    def get_queryset(self):
        queryset = super(RidingStyleListView, self).get_queryset()
        riding_style_id = self.kwargs.get('riding_style_id')
        return queryset.filter(riding_style_id=riding_style_id) if riding_style_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RidingStyleListView, self).get_context_data()
        context['riding_stylies'] = RidingStyle.objects.all()
        return context


class ResumeCreatingView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Resume
    form_class = ResumeCreatingForm
    template_name = 'resumes/creating_resume.html'
    success_url = reverse_lazy('resumes:index')
    success_message = 'Вы успешно зарегистрировались!'
    title = 'SibDoski - Регистрация'
