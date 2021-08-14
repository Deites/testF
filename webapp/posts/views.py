from django.contrib.auth import login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Post
from django.shortcuts import get_object_or_404




class RegisterView(generic.CreateView):
    template_name = 'posts/register.html'
    success_url = reverse_lazy('posts:login')
    form_class = RegisterForm


#reseting password
class PasswordsResetView(PasswordResetView):
    success_url = reverse_lazy('posts:password_reset_done')
    template_name = 'posts/password_reset.html'

class PasswordsResetDoneView(PasswordResetDoneView):
    template_name = 'posts/password_reset_done.html'
    

class PasswordsResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('posts:password_reset_complete')
    template_name = 'posts/password_reset_confirm.html'

class PasswordsResetCompleteView(PasswordResetCompleteView):
    template_name = 'posts/password_reset_complete.html'



class PostsView(LoginRequiredMixin, generic.ListView):
    login_url = 'posts:login'
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-id')

class PostsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    login_url = 'posts:login'
    template_name = 'posts/createpost.html'
    fields = ('topic', 'description', 'photo')
    success_url = reverse_lazy('posts:postsview')

    def form_valid(self, form):
        form.instance.whosePost = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    login_url = 'posts:login'
    template_name = 'posts/comment.html'
    fields = ('comment',)
    success_url = reverse_lazy('posts:postsview')

    def form_valid(self, form):
        form.instance.whose = self.request.user
        form.instance.comment_fk = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    login_url = 'posts:login'
    template_name = 'posts/postupdate.html'
    fields = ('topic', 'description', 'photo')
    success_url = reverse_lazy('posts:postsview')

class PostsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    login_url = 'posts:login'
    success_url = reverse_lazy('posts:postsview')

class PostsDeleteCommentsView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    login_url = 'posts:login'
    
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('posts:postsview'))
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('posts:postsview'))
        comments = Comment.objects.filter(comment_fk=self.kwargs['pk'])
        comments.delete()
        return HttpResponseRedirect('/admin')
    

