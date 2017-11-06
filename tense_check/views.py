from django.shortcuts import render
from .forms import SentenceForm
from .models import Sentence
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .VbPast import preList, preLis2


# def home(request):
#     sentences = Sentence.objects.all()
#     if request.method == 'POST':
#         form = SentenceForm(request.POST)
#         if form.is_valid():
#             sentence_new = form.save(commit=False)
#             sentence_new.save()
#             return HttpResponseRedirect('home')
#     else:
#         form = SentenceForm()
#     return render(request, 'home.html', {'sentences': sentences, 'form': form})

# def home(request):                 # This block commented out here because it is copied below for further development.
#     blogs = Blog.objects.all()     # I will try to process form data before saving it in the database.
#
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog_item = form.save(commit=False)
#             #blog_item.title += 'Looks good!' if 'can' in blog_item.title else 'Maybe you\'re missing something!'
#             blog_item.save()
#             return HttpResponseRedirect('home')
#     else:
#         form = BlogForm()
#
#     # paginator = Paginator(blogs, 15)
#     #
#     # page = request.GET.get('page')
#     # try:
#     #     blogs = paginator.page(page)
#     # except PageNotAnInteger:
#     #     blogs = paginator.page(1)
#     # except EmptyPage:
#     #     blogs = paginator.page(paginator.num_pages)
#     #     return render(request, 'home.html', {'blogs': blogs})
#
#     return render(request, 'home.html', {'blogs': blogs, 'form': form})

# def home(request):
#     sentences = Sentence.objects.all()
#     if request.method == 'POST':
#         form = SentenceForm(request.POST)
#         if form.is_valid():
#             sentence_new = form.save(commit=False)
#             text = sentence_new.text
#             text = text[:-1]
#             text = text.split()
#             i = len(text) - 1
#             in_verbs_one = 'was'
#             in_verbs_two = 'were'
#             in_verbs_three = 'had'
#             in_verbs_four = 'has'
#             in_verbs_five = 'have'
#             in_verbs_six = 'is'
#             in_verbs_seven = 'are'
#             in_verbs_eight = 'am'
#
#             if in_verbs_one in text:
#                 sentence_new.test_res_fail += "Do not use 'was' or 'were' in the past simple tense."
#             elif i == 0:
#                 sentence_new.test_res_fail += 'Too short!'
#             elif in_verbs_two in text:
#                 sentence_new.test_res_fail += "Do not use 'was' or 'were' in the past simple tense."
#             elif in_verbs_four in text:
#                 sentence_new.test_res_fail += "Do not use 'has' or 'have' in the past simple tense."
#             elif in_verbs_five in text:
#                 sentence_new.test_res_fail += "Do not use 'has' or 'have' in the past simple tense."
#             elif in_verbs_six in text:
#                 sentence_new.test_res_fail += "Do not use 'is', 'are' or 'am' in the past simple tense."
#             elif in_verbs_seven in text:
#                 sentence_new.test_res_fail += "Do not use 'is', 'are' or 'am' in the past simple tense."
#             elif in_verbs_eight in text:
#                 sentence_new.test_res_fail += "Do not use 'is', 'are' or 'am' in the past simple tense."
#             elif in_verbs_three in text:
#                 if i == 1:
#                     if text[1] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb'!"
#                     else:
#                         sentence_new.test_res_fail += 'Maybe you\'re missing the object!'
#                 if i == 2:
#                     if text[2] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     else:
#                         sentence_new.test_res_pass += 'Looks good!'
#                 if i == 3:
#                     if text[2] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     elif text[3] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     else:
#                         sentence_new.test_res_pass += 'Looks good!'
#                 if i >= 4:
#                     if text[2] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     elif text[3] in preLis2:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     elif text[4] in preList:
#                         sentence_new.test_res_fail += "Do not use 'had + ed-form of verb' in the past simple."
#                     else:
#                         sentence_new.test_res_pass += 'Looks good!'
#             else:
#                 if i == 1:
#                     if text[1] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     else:
#                         sentence_new.test_res_fail += 'Maybe you\'re missing something!'
#                 if i == 2:
#                     if text[1] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[2] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     else:
#                         sentence_new.test_res_fail += 'Maybe you\'re missing something!'
#                 if i == 3:
#                     if text[1] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[2] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[3] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     else:
#                         sentence_new.test_res_fail += 'Maybe you\'re missing something!'
#                 if i >= 4:
#                     if text[1] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[2] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[3] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     elif text[4] in preList:
#                         sentence_new.test_res_pass += "Looks good!"
#                     else:
#                         sentence_new.test_res_fail += 'Maybe you\'re missing something!'
#             sentence_new.save()
#             return HttpResponseRedirect('home')
#     else:
#         form = SentenceForm()
#
#     paginator = Paginator(sentences, 5)
#
#     page = request.GET.get('page')
#     try:
#         sentences = paginator.page(page)
#     except PageNotAnInteger:
#         sentences = paginator.page(1)
#     except EmptyPage:
#         sentences = paginator.page(paginator.num_pages)
#         return render(request, 'home.html', {'sentences': sentences})
#
#     return render(request, 'home.html', {'sentences': sentences, 'form': form})
#


def home(request):
    sentences = Sentence.objects.all()
    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence_new = form.save(commit=False)
            text = sentence_new.text
            text = text[:-1]
            text = text.split()
            i = len(text) - 1
            in_verbs_one = 'was'
            in_verbs_two = 'were'
            in_verbs_three = 'had'
            in_verbs_four = 'has'
            in_verbs_five = 'have'
            in_verbs_six = 'is'
            in_verbs_seven = 'are'
            in_verbs_eight = 'am'

            if sentence_new.tense_choice == 'past simple positive':
                if in_verbs_one in text:
                    sentence_new.test_res_fail += "Don't use 'was' or 'were' in past simple."
                elif i == 0:
                    sentence_new.test_res_fail += 'Too short!'
                elif in_verbs_two in text:
                    sentence_new.test_res_fail += "Don't use 'was' or 'were' in past simple."
                elif in_verbs_four in text:
                    sentence_new.test_res_fail += "Don't use 'has' or 'have' in past simple."
                elif in_verbs_five in text:
                    sentence_new.test_res_fail += "Don't use 'has' or 'have' in past simple."
                elif in_verbs_six in text:
                    sentence_new.test_res_fail += "Don't use 'is', 'are' or 'am' in past simple."
                elif in_verbs_seven in text:
                    sentence_new.test_res_fail += "Don't use 'is', 'are' or 'am' in past simple."
                elif in_verbs_eight in text:
                    sentence_new.test_res_fail += "Don't use 'is', 'are' or 'am' in past simple."
                elif in_verbs_three in text:
                    if i == 1:
                        if text[1] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb'!"
                        else:
                            sentence_new.test_res_fail += 'Maybe you\'re missing the object!'
                    if i == 2:
                        if text[2] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        else:
                            sentence_new.test_res_pass += 'Looks good!'
                    if i == 3:
                        if text[2] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        elif text[3] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        else:
                            sentence_new.test_res_pass += 'Looks good!'
                    if i >= 4:
                        if text[2] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        elif text[3] in preLis2:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        elif text[4] in preList:
                            sentence_new.test_res_fail += "Don't use 'had + ed-form of verb' in past simple."
                        else:
                            sentence_new.test_res_pass += 'Looks good!'
                else:
                    if i == 1:
                        if text[1] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        else:
                            sentence_new.test_res_fail += 'Maybe you\'re missing something!'
                    if i == 2:
                        if text[1] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[2] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        else:
                            sentence_new.test_res_fail += 'Maybe you\'re missing something!'
                    if i == 3:
                        if text[1] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[2] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[3] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        else:
                            sentence_new.test_res_fail += 'Maybe you\'re missing something!'
                    if i >= 4:
                        if text[1] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[2] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[3] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        elif text[4] in preList:
                            sentence_new.test_res_pass += "Looks good!"
                        else:
                            sentence_new.test_res_fail += 'Maybe you\'re missing something!'
            sentence_new.save()
            return HttpResponseRedirect('home')
    else:
        form = SentenceForm()

    paginator = Paginator(sentences, 20)

    page = request.GET.get('page')
    try:
        sentences = paginator.page(page)
    except PageNotAnInteger:
        sentences = paginator.page(1)
    except EmptyPage:
        sentences = paginator.page(paginator.num_pages)
        return render(request, 'home.html', {'sentences': sentences})

    return render(request, 'home.html', {'sentences': sentences, 'form': form})

