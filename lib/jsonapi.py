"""
tools for managing a JSON API
"""


####################################################################
## DECORATORS

###################################################
## JSONAPI (decorator)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
def jsonapi(func):
    """
    turns a view into a JSON API view (decorator)

    NOTES
    - unless the view returns a HttpResponse object, the response is converted to JSON
    - the view will automatically be `csrf_exempt`
    - if not present a `succes` field is added (value: true)
    """

    @csrf_exempt
    def view(request, *args, **kwargs):

        # call the view function
        data = func(request, *args, **kwargs)

        # if it is already an HttpResponse -> simply return it
        if isinstance(data, HttpResponse): return data

        # otherwise return JSON encoded data
        return JsonResponse(data)

    return view



####################################################################
## CLASSES

###################################################
## DICT RESPONSE (class)
class DictReponse():
    """
    assemble a standardised response dictionary

    NOTE
    - this class has only class methods, there is never a need to instantiate
      an actual object
    - derived classes can for example provide different response templates
    """


    @classmethod
    def _response_template(cls, success, status_message=None):
        """
        creates a template response dict (can be overwritten by derived classes)

        NOTES
        - must always return a dict, possibly and empty one
        """
        resp = {'success': success}
        if not status_message is None: resp['statusmsg'] = status_message
        return resp

    @classmethod
    def _format(cls, data):
        """
        format the data prior to returning it (does nothing)

        NOTES
        - derived classes could eg convert to JSON or YAML
        """
        return data

    @classmethod
    def success(cls, data=None, status_msg=None):
        """
        creates a success response (wraps call to response)
        """
        return cls.response(True, data, status_msg)

    @classmethod
    def error(cls, status_msg=None, data=None):
        """
        creates an error response (wraps call to response)

        """
        return cls.response(False, data, status_msg)

    @classmethod
    def response(cls, success, data=None, status_msg=None):
        """
        creates a generic response

        NOTES
        - data must be a dict (or None)
        - status_msg must a str (or None)
        """
        resp = cls._response_template(success, status_msg)
        if not data is None: resp.update(data)
        return cls._format(resp)
