from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, modelformset_factory
from django.forms import ModelForm

from quiz.models import Choice


class ChoicesInlineFormset(BaseInlineFormSet):
    def clean(self):

        num_correct_answers = sum(form.cleaned_data['is_correct'] for form in self.forms)

        if num_correct_answers == 0:
            raise ValidationError('Необходимо выбрать как минимум 1 вариант.')

        if num_correct_answers == len(self.forms):
            raise ValidationError('Не разрешено выбирать все варианты.')


class QuestionInlineFormset(BaseInlineFormSet):
    def clean(self):
        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError(
                f'Кол-во вопросов должно быть в диапазоне от {self.instance.QUESTION_MIN_LIMIT} '
                f'до {self.instance.QUESTION_MAX_LIMIT} включительно'
            )

        for iteration_num, form in enumerate(self.forms):
            question_num = form.cleaned_data['order_num']

            if iteration_num == 0 and question_num != self.instance.QUESTION_FIRST_NUMBER:
                raise ValidationError(f'Номер первого вопроса должен быть '
                                      f'= {self.instance.QUESTION_FIRST_NUMBER}')

            elif question_num > len(self.forms):
                raise ValidationError('Номер вопроса не может больше кол-ва вопросов в тесте')

            elif question_num != iteration_num + 1:
                raise ValidationError(
                    f'Номер каждого следующего вопроса должен увеличиваться на {self.instance.QUESTION_NUM_STEP}')


class ChoiceForm(ModelForm):
    is_selected = forms.BooleanField(required=False)



    class Meta:
        model = Choice
        fields = ['text', ]


ChoicesFormSet = modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)
