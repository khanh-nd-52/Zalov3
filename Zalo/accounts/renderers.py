import json

from rest_framework import renderers


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        # import pdb
        # pdb.set_trace()
        if 'already exists' in str(data):
            response = json.dumps({'code': '9996', 'message': 'User existed'})
        elif 'more than 10 characters' in str(data):
            response = json.dumps({'code': '1004', 'message': 'Parameter value is invalid'})
        elif 'blank' in str(data):
            response = json.dumps({'code': '1004', 'message': 'Parameter value is invalid'})
        elif 'Ensure this field has at least' in str(data):
            response = json.dumps({'code': '1004', 'message': 'Parameter value is invalid'})
        else:
            response = json.dumps({'code': '1000', 'message': 'OK', 'data': data},)
        return response