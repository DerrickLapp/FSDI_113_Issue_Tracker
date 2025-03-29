from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView
)
from .models import Issue, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Create your views here.
class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "summary", "description", "assignee", "status"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = [
        "name", "summary", "description", "assignee", "status"
    ]

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("board")

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    
class BoardView(LoginRequiredMixin, ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name="to-do")
        in_progress = Status.objects.get(name="in-progress")
        done = Status.objects.get(name="done")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .order_by("created_on").reverse()
        )
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .order_by("created_on").reverse()
        )
        context["done_list"] = (
            Issue.objects
            .filter(status=done)
            .order_by("created_on").reverse()
        )
        return context
    
    
class IssueDetailView(UserPassesTestMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue

    def test_func(self):
        issue = self.get_object()
        if issue.status.name == "done":
            return True
        elif issue.status.name == "to-do" and self.request.user:
            return True
        elif issue.status.name == "in-progress" and self.request.user.is_authenticated:
            return True
        else:
            return False
        