from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Skill


# Create your views here.
def index(request):
    return HttpResponse('Hello World')

@csrf_exempt
def addSkill(request):
    print('hit this addSkill function')
    if request.method == 'POST':
        query = request.POST
        print('query is {}'.format(query))

        if not 'name' in query or not 'description' in query:
            print("ERROR: incorrect query")
            return HttpResponse(status=500)

        new_skill = Skill(
            name=request.POST['name'],
            description=request.POST['description']
        )
        new_skill.save()
        print('saved skill:')
        print(new_skill)
        return HttpResponse(status=200)
    else:
        # TODO: make this error
        return HttpResponse('COULD NOT POST')


def getAllSkills(request):
    skills = Skill.objects.all()
    print('skills are:')
    print(skills)
    dict_skills = []
    for skill in skills:
        dict_skills.append({
            'id': skill.id,
            'name': skill.name,
            'description': skill.description
        })
    return HttpResponse(dict_skills)


def deleteSkill(request, id):
    print('id is: {}'.format(id))
    target_skill = get_object_or_404(Skill, pk=id)
    if isinstance(target_skill, Skill):
        print('target skill is:')
        print(target_skill)
        target_skill.delete()
        return HttpResponse(status=200)
    else:
        return target_skill
