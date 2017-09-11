import http.client
import json
from app_simpl import server_v3_config

__author__ = 'pl'


def remote_call(address, request_obj):
    connection = http.client.HTTPConnection(address)
    args_json = json.dumps(request_obj)
    connection.request('POST', '/' + server_v3_config.api_prefix, args_json)
    response = connection.getresponse()
    status_code = response.status
    ret_json = response.read().decode('utf-8', errors='ignore')
    ret = json.loads(ret_json)
    if status_code != 200:
        raise ChildProcessError(ret)
    if ret.get('error') is not None:
        print(ret)
    return ret
