
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.html import escape
def getB(self, request, *args, **kwds):
        context = self.get_context_data()

        text = request.GET['text']
        text = text.replace('"', '')

        # ruleid: raw-html-format
        context['html'] = '<a href="http://external/abc/' + text + '">Check link href</a>'

        return render(request, self.template_name, context)
