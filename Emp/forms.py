from Emp.models import UsrRg,NewData
from django import forms
class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"enter username","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email",})
		}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"update username","required":True}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age","required":True}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"update email"})
		}
class NewUsrForm(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={
		"mobile":forms.TextInput(attrs={"class":"form-control","placeholder":"update urmobilenumber","max":10}),
		"gender":forms.Select(attrs={"class":"form-control",}),
		}




