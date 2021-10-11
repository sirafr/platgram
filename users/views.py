"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy,reverse
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    """USERS SIGN UP VIEW"""

    template_name= 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        """SAVE FORM DATA"""

        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin,UpdateView):
    """UPDATE PROFILE VIEW"""
    template_name = "users/update_profile.html"
    model = Profile
    fields = ['website','biography','phone_number','picture']

    def get_object(self):
        """Return users's profile"""
        
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""

        username = self.object.user.username
        return reverse('users:detail',kwargs={'username':username})

class LoginView(auth_views.LoginView):
    """LOGIN VIEW"""

    template_name = 'users/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({
            'class': 'form-control'})
        form.fields['password'].widget.attrs.update({
            'class': 'form-control'})
        return form

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if request.user.is_authenticated:
            return redirect('posts:feed')
        return super().get(request, args, kwargs)

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """LOGOUT VIEW"""

    template_name = 'users/logged_out.html'