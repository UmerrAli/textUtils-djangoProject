# I have created this file - Umer
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyzetext(request):
    # getting text and other operation to perfrom on text
    original_text = request.POST.get('text', 'default')
    remove_punctuations = request.POST.get('RemovePunctuations', 'off')
    cap = request.POST.get('Cap', 'off')
    remove_Space = request.POST.get('rmSpace', 'off')
    newlineremover = request.POST.get('rmNewLine', 'off')
    charcount = request.POST.get('charcount', 'off')

    if remove_punctuations == 'on':
        analyzed_text = ''
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in original_text:
            if i not in punctuations:
                analyzed_text = analyzed_text + i
        params = {'analyzed_text': analyzed_text}
    else:
        analyzed_text = original_text

    if cap == 'on':
        analyzed_text2 = ''
        for char in analyzed_text:
            analyzed_text2 = analyzed_text2 + char.upper()
        params = {'analyzed_text': analyzed_text2}
    else:
        analyzed_text2 = analyzed_text

    if remove_Space == 'on':
        analyzed_text3 = ""
        for index, char in enumerate(analyzed_text2):
            if not (analyzed_text2[index] == " " and analyzed_text2[index + 1] == " "):
                analyzed_text3 = analyzed_text3 + char
        params = {'analyzed_text': analyzed_text3}
    else:
        analyzed_text3 = analyzed_text2

    if newlineremover == 'on':
        analyzed_text4 = ""
        for char in analyzed_text3:
            if char != '\n' and char != '\r':
                analyzed_text4 = analyzed_text4 + char
        params = {'analyzed_text': analyzed_text4}
    else:
        analyzed_text4 = analyzed_text3

    if charcount == 'on':
        analyzed_text5 = ''
        alpha = 0
        digit = 0
        for i in analyzed_text4:
            if i.isalpha():
                alpha = alpha + 1
            elif i.isdigit():
                digit = digit + 1
        analyzed_text5 = analyzed_text4 + "\n" + f'Text contains {alpha} alphabets and {digit} digits'
        params = {'analyzed_text': analyzed_text5}

    if charcount == 'off' and newlineremover == 'off' and remove_Space == 'off' and cap == 'off' and remove_punctuations == 'off':
        params = {'analyzed_text': ' '}

    return render(request, 'analyzedText.html', params)
