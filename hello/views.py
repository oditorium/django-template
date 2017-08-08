from django.http import HttpResponse

import logging
logger    = logging.getLogger(__name__)
loggerd   = logging.getLogger('data')


def hello(request):
    logger.info("Hello World was called")
    loggerd.info("{'called': 'Hello World'}")
    return HttpResponse('Hello World!')
