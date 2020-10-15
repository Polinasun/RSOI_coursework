import logging
from .base_view import BaseView
from ..models import DancersLog, ClubsLog, CompetitionsLog
import json
import requests
from ..tasks import add_entry_stat
from django.conf import settings

log = logging.getLogger('delete_log')

class ClubsStatView(BaseView):

    def get(self, request, uuid):
        params = request.GET
        result = []
        data = DancersLog.objects.filter(method='PATCH').values()
        for log in data:
            log_data = json.loads(log['data'])
            if str(uuid) in log_data['url']:
                if log_data.get('club'):
                    result.append({'time': log['time'], 'club': log_data['club']})
        
        for club in result:
            club['club'] = request.get(settings.CLUBS_SERVICE_BASE_URL + 'clubs/club/{}/'.format(club['club'])).json()['name']
        
        return result