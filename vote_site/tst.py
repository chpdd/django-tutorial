from polls.models import Choice, Question

Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new", pub_date=timezone.now())

q.save()
print(q.id)
print(q.question_text)
print(q.pub_date)
print(q.question_text)
q.save()
Question.objects.all()
