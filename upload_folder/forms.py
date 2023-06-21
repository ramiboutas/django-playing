from django.forms import ModelForm


from .models import FolderContent

class FolderContentForm(ModelForm):

    class Meta:
        model = FolderContent