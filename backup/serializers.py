from rest_framework import serializers

from backup.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'name', 'email_home', 'email_work', 'phone_home', 'phone_work',
            'address_home', 'address_work', 'date_of_birth', 'company',
            'job_title')
