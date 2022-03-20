import json
import requests

from config import base_url
from helpers import save_data


def get_active_validators():
    url = '/validators'
    r = requests.get(f'{base_url}{url}')
    data = r.json()
    result = [v for v in data if v['status'] == 'BOND_STATUS_BONDED']
    return result


def get_delegations(validator_address, min_anount=50000000000):
    url = f'/validators/{validator_address}/delegations'
    r = requests.get(f'{base_url}{url}')
    data = r.json()
    result = [x for x in data if x['amount']['denom'] ==
              'uumee' and x['amount']['amount'] > min_anount]
    return result


if __name__ == '__main__':
    active_validators = get_active_validators()
    save_data(active_validators, 'active_validators')

    for v in active_validators:
        delegations_data = get_delegations(v['operator_address'])
        save_data(delegations_data, f'delegations_data_{v["moniker"]}')
