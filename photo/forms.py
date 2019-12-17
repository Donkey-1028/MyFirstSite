from photo.models import *
from django.forms.models import inlineformset_factory

# InlineFormset이란 메인 Form에 딸려있는 하위 Formset.
# 1:N 테이블일 경우 N 테이블의 여러 레코드를 한번에 입력받기 위한 폼.
PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title', 'description'],
                                           extra=2
                                           )
