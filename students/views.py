
# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

logger = logging.getLogger(__name__)

class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def	get_queryset(self):
		qs =  super(StudentListView, self).get_queryset()
		course_id =self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses__id=course_id)
		return qs


class StudentDetailView(DetailView):
	model = Student
	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		logger.debug('Students detail view has been debugged')
		logger.info('Logger of students detail view informs you!')
		logger.warning('Logger of students detail view warns you!')
		logger.error('Students detail view went wrong!')
		return context

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = u'Student registration'
		return context

	def form_valid(self, form):
		application = form.save()
		message = u'Student %s %s has been successfully added.' % (application.name, application.surname)
		messages.success(self.request, message)
		return super(StudentCreateView, self).form_valid(form)


# def create(request):
# 	if request.method == 'POST':
# 		form = StudentModelForm(request.POST)
# 		if form.is_valid():
# 			student = form.save()
# 			message = u"Student %s %s has been successfully added." %(student.name, student.surname)
# 			messages.success(request, message)
# 			return redirect('students:list_view')
# 	else:
# 		form = StudentModelForm()

# 	return render(request, 'students/add.html', {'form':form})
class StudentUpdateView(UpdateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = u'Student info update'
		return context

	def form_valid(self, form):
		application = form.save()
		message = u'Info on the student has been sucessfully changed.'
		messages.success(self.request, message)
		return super(StudentUpdateView, self).form_valid(form)

# def edit(request,id):
# 	student_inst=Student.objects.get(pk=id)
# 	if request.method == 'POST':
# 		form = StudentModelForm(request.POST, instance=student_inst)
# 		if form.is_valid():
# 			student= form.save()
# 			message = u"Info on the student has been sucessfully changed."
# 			messages.success(request, message)
# 			return redirect('students:list_view')
# 	else:
# 		form = StudentModelForm(instance=student_inst)
	
# 	return render(request,"students/edit.html",{"form":form})
 
class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Student info suppression'
		return context 

# def remove(request,id):
#     student=Student.objects.get(pk=id)
#     if request.method == 'POST':
#         student.delete
#         ()
#         message = u"Info on %s %s has been sucessfully deleted." %(student.name, student.surname)
#         messages.success(request, message)
#         return redirect('students:list_view')
#     return render(request,"students/remove.html",{"student":student})






# def list_view(request):
#     if request.GET:
#         student = Student.objects.filter(courses__id=int(request.GET['course_id']))
#     else:
#         student = Student.objects.all()
#     return render(request, 'students/list.html', {'students': student})

# def detail(request, student_id):
#     student = Student.objects.get(id=student_id)
#     return render(request, 'students/detail.html', {'student': student})
