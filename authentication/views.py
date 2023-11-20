from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .form import CreateUserForm, EditProfile, CreateProfileForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from core.models import Profile



# Create your views here.
class Register(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class UserEditProfile(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *arg, **kwargs):
        page_user = Profile.objects.all()
        context  = super(ShowProfilePageView, self).get_context_data(*arg, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
class EditUserProfile(generic.UpdateView):
    model = Profile
    template_name = 'registration/user_edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('home')

class CreateProfile(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

