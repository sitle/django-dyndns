from django.http import HttpResponse
from django.template import RequestContext, loader

from log2dyndns import Log2DynDns

def index(request):
    userdyndns = ''
    password = ''
    laclass = Log2DynDns()
    laclass.set_site('https://account.dyn.com')
    laclass.set_account(userdyndns)
    laclass.set_password(password)
    laclass.do_connect()

    template = loader.get_template('dyndns/index.html')

    list_hosts = laclass.get_hosts()

    context = RequestContext(request, {
      'userdyndns': userdyndns,
      'list_hosts': list_hosts,
    })
    return HttpResponse(template.render(context))

