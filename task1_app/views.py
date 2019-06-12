from django.shortcuts import render
from .models import Node
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def nodelist(request):
    nodes = Node.objects.all()

    if request.is_ajax():
        parent_node = request.POST.get('parent_node')
        parent_node_pk = Node.objects.get(name=parent_node)
        newnode = Node(
            name= chr(ord(nodes[len(nodes) - 1].name) + 1),
            from_to=str(parent_node_pk.pk)+'-'+ str(nodes[len(nodes)-1].pk + 1)
        )
        newnode.save()
        all_nodes = []
        for i in range(len(nodes)):
            node = {}
            node['name']=nodes[i].name
            node['from_to']=nodes[i].from_to
            all_nodes.append(node)

        output = {'all_nodes':all_nodes,'new_node':{'newnode_name':newnode.name, 'newnode_from_to':newnode.from_to}}
        return HttpResponse(json.dumps(output), content_type='text')
    return render(request, 'task1_app/index.html',{'nodes':nodes})


def all_nodes(request):
    nodes = Node.objects.all()
    if request.is_ajax():
        all_nodes = []
        for i in range(len(nodes)):
            node = {}
            node['name'] = nodes[i].name
            node['from_to'] = nodes[i].from_to
            all_nodes.append(node)
        print(all_nodes)
        return HttpResponse(json.dumps(all_nodes), content_type='text')
    return HttpResponse('asd')