from django.shortcuts import render
from .models import HiddenNumbers, guesswork, PowerOfAttorney
from .forms import HiddenNumbersForm
import random


def index(requset):
    number = HiddenNumbers.objects.order_by('-id')[:5]
    guess = guesswork.objects.order_by('-id')[:5]
    attorney = PowerOfAttorney.objects.order_by('-id')[:1]

    witch = Random()
    witch1 = Random()
    attorney1 = 0
    attorney2 = 0

    for el in attorney:
        attorney1 = el.attorney_1
        attorney2 = el.attorney_2
        break

    if (requset.method == 'POST'):
        form_Number = HiddenNumbersForm(requset.POST)
        if (is_digit(form_Number['numbers'].value())) and form_Number.is_valid():
            num = int(form_Number['numbers'].value())

            guesswork(witch_1=witch, witch_2=witch1).save()
            form_Number.save()
            if num != witch:
                x = int(attorney1)-1
            else:
                x = int(attorney1)+1

            if num != witch:
                y = int(attorney2)-1
            else:
                y = int(attorney2)+1
            PowerOfAttorney(attorney_1=x, attorney_2=y).save()

    form = HiddenNumbersForm()

    context = {
        'HiddenNumbers': number,
        'guesswork': guess,
        'attorney': attorney,
        'form': form,
    }

    return render(requset, 'main/indecx.html', context)


def is_digit(string):
    if len(string) < 2:
        return False

    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def Random():
    return random.randint(10, 99)
