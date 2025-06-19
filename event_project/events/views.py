from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
from django.core.mail import send_mail


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location', 'date']
    search_fields = ['title', 'description']
    ordering_fields = ['date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        registration = serializer.save()
        user_email = registration.user.email
        event_title = registration.event.title
        event_date = registration.event.date
        event_location = registration.event.location

        send_mail(
            subject= 'Event Registration Confirmation',
            message= (
                f'Hello {registration.user.username},\n\n'
                f'You have successfully registered for the event:\n'
                f'- Title: {event_title}\n'
                f'- Date: {event_date}\n'
                f'- Location: {event_location}\n\n'
                f'Thank you for using our service!'
            ),
            from_email=None,
            recipient_list=[user_email],
            fail_silently=False,
        )
# Create your views here.
