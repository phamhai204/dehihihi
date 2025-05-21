from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment, Profile
from django.utils import timezone
from django.db import IntegrityError

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Appointment Date & Time'
    )

    class Meta:
        model = Appointment
        fields = ['service', 'barber', 'appointment_date', 'notes']

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        now = timezone.now()
        if appointment_date < now:
            raise forms.ValidationError("Bạn không thể đặt lịch ở quá khứ.")
        return appointment_date

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, label="Số điện thoại", required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Số điện thoại này đã được sử dụng.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit)
        phone_number = self.cleaned_data["phone_number"]
        try:
            Profile.objects.create(user=user, phone_number=phone_number)
        except IntegrityError:
            self.add_error('phone_number', "Số điện thoại này đã được sử dụng.")
            user.delete()  # Xóa user vừa tạo nếu lỗi
            raise forms.ValidationError("Số điện thoại này đã được sử dụng.")
        return user