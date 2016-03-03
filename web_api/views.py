# coding=utf-8
from web_modles import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def urls(request):
    if request.method == "GET":
        urls_obj = models.Url.objects.values("name","url")
        url_list = list(urls_obj)
        return HttpResponse(json.dumps({"data": url_list}))

    elif request.method == "POST":

        datas = request.POST.get("data", None)
        hostname = request.POST.get("hostname", None)
        agent, is_have = models.Agent.objects.get_or_create(hostname=hostname)
        for data in json.loads(datas):
            url = models.Url.objects.filter(url=data["url"]).get()
            models.Record.objects.update_or_create(url=url,agent=agent,code=data["code"])
        return HttpResponse(datas)