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

        parent_skill = None

        if 'parent_id' in query:
            parent_skill_id = query['parent_id']
            parent_skill = get_object_or_404(Skill, pk=parent_skill_id)
            if not isinstance(parent_skill, Skill):
                print('no skill with id: {}'.format(parent_skill_id))
                return parent_skill


        new_skill = Skill(
            name=query['name'],
            description=query['description'],
            parent_skill=parent_skill
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
            'description': skill.description,
            'parent_skill': skill.parent_skill
        })
    return HttpResponse(dict_skills)


def printSkillTrees(request):
    # first get root nodes
    root_nodes = Skill.objects.filter(parent_skill__isnull=True)
    print('all root nodes:')
    print(root_nodes)

    skill_trees = []


    for skill in root_nodes:
        tree = makeSkillTree(skill)
        skill_trees.append(tree)

    return HttpResponse(skill_trees)

def makeSkillTree(skill):
    tmp = {
        'skill': skill,
        'child_skills': []
    }
    children = skill.skill_set.all()
    for child in children:
        tmp['child_skills'].append(makeSkillTree(child))

    return tmp


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


@csrf_exempt
def deleteSkillByName(request):
    if request.method == 'POST':
        query = request.POST
        try:
            target_skill = Skill.objects.get(name=query['name'])
            target_skill.delete()
        except Skill.DoesNotExist:
            print("skill not found for deleting")
    else:
        print("NOT POST!!!!")
        return HttpResponse(status=500)

    return HttpResponse(status=200)
