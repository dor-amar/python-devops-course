"""Basic Django operations module."""

import os
import sys
from typing import Any, Dict, List, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from django import setup
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.management.commands import startproject, startapp
from django.db import models
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class DjangoProjectManager:
    """Manager for Django project operations."""

    def __init__(self, project_name: str = "myproject"):
        """Initialize the Django project manager.

        Args:
            project_name: Name of the Django project
        """
        self.project_name = project_name
        self.project_dir = Path(project_name)
        self._setup_django()

    def _setup_django(self) -> None:
        """Set up Django environment."""
        if not settings.configured:
            settings.configure(
                DEBUG=True,
                SECRET_KEY=os.getenv('DJANGO_SECRET_KEY', 'dev'),
                ROOT_URLCONF=f'{self.project_name}.urls',
                INSTALLED_APPS=[
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'blog',  # Our example app
                ],
                MIDDLEWARE=[
                    'django.middleware.security.SecurityMiddleware',
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                    'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                ],
                TEMPLATES=[
                    {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        'DIRS': [],
                        'APP_DIRS': True,
                        'OPTIONS': {
                            'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                            ],
                        },
                    },
                ],
                WSGI_APPLICATION=f'{self.project_name}.wsgi.application',
                DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': self.project_dir / 'db.sqlite3',
                    }
                },
                AUTH_PASSWORD_VALIDATORS=[
                    {
                        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
                    },
                    {
                        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                    },
                    {
                        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
                    },
                    {
                        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
                    },
                ],
                LANGUAGE_CODE='en-us',
                TIME_ZONE='UTC',
                USE_I18N=True,
                USE_TZ=True,
                STATIC_URL='static/',
                DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
            )
            setup()

    def create_project(self) -> None:
        """Create a new Django project."""
        if self.project_dir.exists():
            console.print(f"[yellow]Project {self.project_name} already exists[/]")
            return

        console.print(f"[green]Creating Django project: {self.project_name}[/]")
        execute_from_command_line([
            'django-admin',
            'startproject',
            self.project_name
        ])

    def create_app(self, app_name: str) -> None:
        """Create a new Django app.

        Args:
            app_name: Name of the app to create
        """
        app_dir = self.project_dir / app_name
        if app_dir.exists():
            console.print(f"[yellow]App {app_name} already exists[/]")
            return

        console.print(f"[green]Creating Django app: {app_name}[/]")
        execute_from_command_line([
            'manage.py',
            'startapp',
            app_name
        ])

    def create_models(self) -> None:
        """Create example models for the blog app."""
        models_file = self.project_dir / 'blog' / 'models.py'
        if not models_file.exists():
            console.print("[red]Blog app not found[/]")
            return

        models_file.write_text('''
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """Blog post category."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """Blog post."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        default='draft'
    )

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Blog post comment."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
        ''')

    def create_views(self) -> None:
        """Create example views for the blog app."""
        views_file = self.project_dir / 'blog' / 'views.py'
        if not views_file.exists():
            console.print("[red]Blog app not found[/]")
            return

        views_file.write_text('''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post, Category, Comment


class PostListView(ListView):
    """List view for blog posts."""

    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    """Detail view for a blog post."""

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context


@login_required
def add_comment(request, post_id):
    """Add a comment to a post."""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            return redirect('post_detail', slug=post.slug)
    return redirect('post_detail', slug=post.slug)


def category_posts(request, category_slug):
    """List posts in a category."""
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status='published')
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts
    })
        ''')

    def create_urls(self) -> None:
        """Create URL patterns for the blog app."""
        urls_file = self.project_dir / 'blog' / 'urls.py'
        if not urls_file.exists():
            console.print("[red]Blog app not found[/]")
            return

        urls_file.write_text('''
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
        ''')

    def create_templates(self) -> None:
        """Create example templates for the blog app."""
        templates_dir = self.project_dir / 'blog' / 'templates' / 'blog'
        templates_dir.mkdir(parents=True, exist_ok=True)

        # Base template
        base_template = templates_dir / 'base.html'
        base_template.write_text('''
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Blog{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'blog:post_list' %}">Blog</a>
            <div class="navbar-nav">
                <a class="nav-link" href="{% url 'blog:post_list' %}">Home</a>
                {% if user.is_authenticated %}
                    <a class="nav-link" href="{% url 'admin:index' %}">Admin</a>
                    <a class="nav-link" href="{% url 'admin:logout' %}">Logout</a>
                {% else %}
                    <a class="nav-link" href="{% url 'admin:login' %}">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
        ''')

        # Post list template
        post_list_template = templates_dir / 'post_list.html'
        post_list_template.write_text('''
{% extends 'blog/base.html' %}

{% block title %}Blog Posts{% endblock %}

{% block content %}
    <h1>Blog Posts</h1>
    {% for post in posts %}
        <article class="card mb-4">
            <div class="card-body">
                <h2 class="card-title">
                    <a href="{% url 'blog:post_detail' post.slug %}">
                        {{ post.title }}
                    </a>
                </h2>
                <p class="card-text">
                    By {{ post.author.username }} on {{ post.published_at|date }}
                </p>
                <p class="card-text">{{ post.content|truncatewords:50 }}</p>
                <a href="{% url 'blog:post_detail' post.slug %}" class="btn btn-primary">
                    Read more
                </a>
            </div>
        </article>
    {% empty %}
        <p>No posts found.</p>
    {% endfor %}

    {% if is_paginated %}
        <nav>
            <ul class="pagination">
                {% if page_obj.has_previous %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                            Previous
                        </a>
                    </li>
                {% endif %}

                {% for num in page_obj.paginator.page_range %}
                    <li class="page-item {% if page_obj.number == num %}active{% endif %}">
                        <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                    </li>
                {% endfor %}

                {% if page_obj.has_next %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                            Next
                        </a>
                    </li>
                {% endif %}
            </ul>
        </nav>
    {% endif %}
{% endblock %}
        ''')

    def run_migrations(self) -> None:
        """Run database migrations."""
        console.print("[green]Running database migrations...[/]")
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])

    def create_superuser(self) -> None:
        """Create a superuser for the admin interface."""
        console.print("[green]Creating superuser...[/]")
        execute_from_command_line(['manage.py', 'createsuperuser'])

    def run_server(self) -> None:
        """Run the development server."""
        console.print("[green]Starting Django development server...[/]")
        execute_from_command_line(['manage.py', 'runserver'])


# Example usage
if __name__ == "__main__":
    try:
        # Initialize Django project manager
        manager = DjangoProjectManager()

        # Create project
        manager.create_project()

        # Create blog app
        manager.create_app('blog')

        # Create models
        manager.create_models()

        # Create views
        manager.create_views()

        # Create URLs
        manager.create_urls()

        # Create templates
        manager.create_templates()

        # Run migrations
        manager.run_migrations()

        # Create superuser
        manager.create_superuser()

        # Run server
        manager.run_server()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 