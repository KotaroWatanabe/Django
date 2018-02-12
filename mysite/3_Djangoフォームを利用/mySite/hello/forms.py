from django import forms


class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='name',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    
######################################################
EMPTY_CHOICES = (
    ('', '-'*10),
)

GENDER_CHOICES = (
    ('man', 'men'),
    ('woman', 'women')
)

FOOD_CHOICES = (
    ('apple', 'apple'),
    ('beef', 'meet'),
    ('bread', 'bread'),

)


class SampleForm(forms.Form):
    age = forms.IntegerField(
        label='age',
        min_value=0,
        max_value=200,
        required=True,
    )

    birthday = forms.DateField(
        label='birth',
        required=True,
        input_formats=[
            '%Y-%m-%d',  # 2010-01-01
            '%Y/%m/%d',  # 2010/01/01
        ]
    )

    send_message = forms.BooleanField(
        label='send',
        required=False,
    )

    gender_r = forms.ChoiceField(
        label='sex',
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
        required=True,
    )

    gender_s = forms.ChoiceField(
        label='sex',
        widget=forms.Select,
        choices=EMPTY_CHOICES + GENDER_CHOICES,
        required=False,
    )

    food_s = forms.ChoiceField(
        label='food',
        widget=forms.SelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )

    food_c = forms.ChoiceField(
        label='food',
        widget=forms.CheckboxSelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )