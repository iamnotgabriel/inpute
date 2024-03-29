from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView, CreateView, ListView, RedirectView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Question, Answer
from .forms import AnswerForm, UpdatePostForm

class QuestionView(LoginRequiredMixin ,DetailView):
    model = Question
    content_object_name = 'question'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields =['title', 'description']

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk        
        return super().form_valid(form)

@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('post_detail', pk = question.pk)
    else:
        form = AnswerForm()
    return render(request, 'posts/add_answer.html', {'form': form})


class QuestionListView(LoginRequiredMixin ,ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date']

def change_post(request, pk):
    post = get_object_or_404(Question, pk = pk)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance= post)
        if form.is_valid():
            post =  form.save(commit = False)
            post.date = timezone.now()
            post.user = request.useredit_
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = UpdatePostForm(instance = post) 
        return render(request, 'posts/post_edit.html', {'form': form})


@login_required
@csrf_exempt
def verify(request, back,pk):
    answer = get_object_or_404(Answer, pk=pk)
    data ={}
    data['btn_id'] = '#v-'+str(pk)
    if request.user.profile.is_monitor:
        answer.verified = not answer.verified
        answer.save()
    if answer.verified:
        data['btn_class'] = 'save btn btn-success'
        data['btn_text'] = 'Verificado'
    else:
        data['btn_class'] = 'save btn btn-default'
        data['btn_text'] = 'Verificar'
    return JsonResponse(data)