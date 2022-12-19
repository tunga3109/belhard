from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.decorators.http import require_GET

from .models import Post, Contact
from .forms import ContactForm, MyForm


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'github': 'https://github.com'
    }


class PostListView(BaseMixin, ListView):
    template_name = "blog/index.html"
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'MIXIN HEADING'
        context['subheading'] = 'mixin subheading'
        context['form'] = ContactForm()
        context['my_form'] = MyForm()
        context.update(self.context)
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('form_type') == 'contact_form':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get('form_type') == 'email_form':
            print(request.POST.get('email'))

        return self.get(request=request)


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class AboutTemplateView(BaseMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'About'
        context['coordinate'] = 'https://www.google.com/maps/d/embed?mid=1_ECVm1j8vq8hcyTlEPFP_wGe2Hk&hl=ru&ehbc=2E312F'
        context['about'] = '''
                aboutaboutaboutaboutaboutaboutaboutaboutabout
                aboutaboutaboutaboutaboutaboutaboutaboutabout
                aboutaboutaboutaboutaboutaboutaboutaboutabout
                aboutaboutaboutaboutaboutaboutaboutaboutabout
                aboutaboutaboutaboutaboutaboutaboutaboutabout
        '''
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'blog/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('blog_posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'Contact'
        return context


# @require_GET
# def blog_list(request: HttpRequest):
#     posts_list = Post.objects.all()
#     return render(request, "blog/index.html", {'posts': posts_list})


# def post_detail(request: HttpRequest, post_slug: str):
#     post = get_object_or_404(Post, slug=post_slug)
#     return render(request, 'blog/post.html', {'post': post})


# def contact(request: HttpRequest):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = ContactForm()
#     return render(request, 'blog/contact.html', {'contact_form': form})


# def about(request: HttpRequest):
#     return render(request, 'blog/about.html')


def error404(request, exception):
    return render(request, 'blog/error_404.html')
