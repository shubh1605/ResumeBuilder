from __future__ import print_function
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from testing.utils import render_to_pdf
from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template
from .utils import render_to_pdf

from wkhtmltopdf.views import PDFTemplateResponse

import pdfkit

def home(request):
	# pdfkit.from_file('D   :/Django/resumeBuilder/testing/templates/testing/home.html','nohope.pdf')
	return render(request, 'testing/home.html', {'temp':'testing\\files\\template1\\temp1.html'})

def test(request):
	return render(request, 'testing/files/template2/temp2.html', {'temp':'/testing/testing.html'})


class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('testing/files/template2/temp2.html')
		context = {
			"first_name": 'Shubh Gangar',
		}
		html = template.render(context)
		pdf = render_to_pdf('testing/files/template2/temp2.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" %("12341231")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")




