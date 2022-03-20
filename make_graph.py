from pyvis.network import Network
import pandas as pd

from helpers import read_data


net = Network(height='750px', width='100%',
              bgcolor='#222222', font_color='white')

net.barnes_hut()

delegations_data = pd.read_csv('data/network_delegations.csv')
validators_data = read_data('active_validators')

sources = delegations_data['Source']
targets = delegations_data['Target']
weights = delegations_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net.add_node(src, src, title=src, group=1)
    net.add_node(dst, dst, title=dst, group=2)

    amount_k = round(w/10**9, 2)
    net.add_edge(src, dst, value=w, title=f"{amount_k:,}K umee")

neighbor_map = net.get_adj_list()

for node in net.nodes:
    # node['value'] = len(neighbor_map[node['id']])
    tokens = 0
    for v in validators_data:
        if node['title'] == v['moniker']:
            tokens = v['tokens']
            # node['image'] = v['avatar']
            # node['shape'] = 'circularImage'
    if tokens:
        node['value'] = tokens
    else:
        node['value'] = len(neighbor_map[node['id']])
    node['title'] += '<br>Delegations:<br>' + \
        '<br>'.join(neighbor_map[node['id']])


# net.show_buttons()
net.show('umee_delegations_small.html')
