import logging
from .base_view import BaseView
from ..models import DancersLog, ClubsLog, CompetitionsLog
import json
import requests
from ..tasks import add_entry_stat

log = logging.getLogger('delete_log')


class LogsView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, **params):
        services = {'Clubs': ClubsLog, 'Dancers': DancersLog, 'Competitions': CompetitionsLog}
        params = request.GET
        service = request.headers.get('Service')
        if service:
            model = services.get(service)
            if model:
                response = list(model.objects.filter(**params).values())
                return {'status': 'Success', 'data': response, 'code': 200}
            else:
                return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
        

    @BaseView.authorization(('admin', 'anonymous'))
    def post(self, request, client_id, client):
        services = {'Clubs': ClubsLog, 'Dancers': DancersLog, 'Competitions': CompetitionsLog}
        params = request.GET
        service = request.headers.get('Service')
        if service:
            model = services.get(service)
            if model:
                data = json.loads(request.body.decode('utf-8'))
                add_entry_stat.delay(service, data)
                # response = model.objects.create(**data).pk
                return {'status': 'Success', 'code': 200}
            else:
                return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
        else:
            return {'status': 'Failed', 'message': 'Bad request', 'code': 400}

class LogView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, uuid, **params):
        services = {'Clubs': ClubsLog, 'Dancers': DancersLog, 'Competitions': CompetitionsLog}
        service = request.headers.get('Service')
        if service:
            model = services.get(service)
            if model:
                response = list(DancersLog.objects.filter(pk=uuid).values())
                if not response:
                    return {'status': 'Failed', 'message': 'Object does not exist', 'code': 404}
                return {'status': 'Success', 'data': response, 'code': 200}
            else:
                return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
        else:
            return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
            
    @BaseView.authorization(('admin', 'anonymous'))
    def delete(self, request, uuid, client_id, client):
        services = {'Clubs': ClubsLog, 'Dancers': DancersLog, 'Competitions': CompetitionsLog}
        service = request.headers.get('Service')
        if service:
            model = services.get(service)
            if model:
                entry = DancersLog.objects.filter(pk=uuid)
                entry.delete()
                BaseView.log(log, request, client, client_id)
                return {'status': 'Success', 'code': 200}
            else:
                return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
        else:
            return {'status': 'Failed', 'message': 'Bad request', 'code': 400}
            