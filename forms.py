from django import forms

class RestaurantAdditionForm(forms.Form):
    restaurant_name = forms.CharField(label='restaurant_name', max_length=50, required=True)
    # restaurant_open_hour = forms.CharField(label='restaurant_open_hour', required=False)
    # restaurant_close_hour = forms.CharField(label='restaurant_close_hour', required=False)
    restaurant_address = forms.CharField(label='restaurant_address', max_length=50, required=True)
    restaurant_phone = forms.CharField(label='restaurant_phone', max_length=20, required=True)
    restaurant_email = forms.CharField(label='restaurant_email', max_length=50, required=False)
    restaurant_category = forms.CharField(label='restaura nt_category', max_length=20, required=False)
    restaurant_description = forms.CharField(label='restaurant_description', max_length=200, required=False)

class RestaurantAdvanceForm(forms.Form):
    restaurant_name = forms.CharField(label='restaurant_name', max_length=50)
    restaurant_open_hour = forms.CharField(label='restaurant_open_hour', required=False)
    restaurant_close_hour = forms.CharField(label='restaurant_close_hour', required=False)
    restaurant_address = forms.CharField(label='restaurant_address', max_length=50)
    restaurant_phone = forms.CharField(label='restaurant_phone', max_length=20)
    restaurant_email = forms.CharField(label='restaurant_email', max_length=50, required=False)
    restaurant_category = forms.CharField(label='restaura nt_category', max_length=20, required=False)
    restaurant_description = forms.CharField(label='restaurant_description', max_length=200, required=False)
    restaurant_score = forms.FloatField(label='restaurant_score',required=False)
    restaurant_area = forms.CharField(label='restaurant_area', max_length=50, required=False)
    restaurant_revenue = forms.DecimalField(label='restaurant_revenue',required=False)
    restaurant_numofrecommendation = forms.IntegerField(label='restaurant_numofrecommendation',required=False)
    restaurant_picture = forms.CharField(label='restaurant_picture',required=False)

