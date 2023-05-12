from django.urls import path

from resumes.views import ResumeCreatingView, RidingStyleListView, ResumeDetailsView, OrderCreatingView

app_name = 'resumes'

urlpatterns = [
    path('', RidingStyleListView.as_view(), name='index'),
    path('creating/', ResumeCreatingView.as_view(), name='creating'),
    path('riding_style/<int:riding_style_id>/', RidingStyleListView.as_view(), name='riding_style'),
    path('page/<int:page>/', RidingStyleListView.as_view(), name='paginator'),
    path('resume/<int:resume_id>/', ResumeDetailsView.as_view(), name='resume_detail'),
    path('resume/create_order/<int:resume_id>/', OrderCreatingView.as_view(), name='create_order'),
]
