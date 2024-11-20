   def get4(self, request, *args, **kwds):
        context = self.get_context_data()

        text = request.GET['text']
        text = text.replace('"', '')

        # ruleid: raw-html-format
        context['html'] = '<a href="http://external/abc/%s">Check link href</a>'.format(text)

        return render(request, self.template_name, context)
