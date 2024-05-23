from django.urls import path

from .views import EmailExtractionViewSet

app_name = 'nickname_extraction_service'

urlpatterns = [
    path('emails/nickname',
         EmailExtractionViewSet.as_view(
             {'post': 'post_emails_nickname', 'get': 'get_emails_nickname'}
         ),
         name='nicknames'),

    path('emails/domain',
         EmailExtractionViewSet.as_view(
             {'post': 'post_emails_domain', 'get': 'get_emails_domain'}
         ),
         name='domains'),
]
