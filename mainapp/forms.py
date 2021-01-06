from django import forms
from crispy_forms.helper import FormHelper
from .models import Feedback, MerchantFeedback

 
class FeedbackForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = Feedback
        fields = "__all__"


class MerchantFeedbackForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = MerchantFeedback
        fields = "__all__"