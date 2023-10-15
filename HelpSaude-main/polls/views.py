from django.http import HttpResponse
from django.template import loader
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('public_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))
