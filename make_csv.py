import pandas as pd

from helpers import save_data, read_data


def convert_data():
    result = []
    active_validators = read_data('active_validators')
    for v in active_validators:
        delegations_data = read_data(f'delegations_data_{v["moniker"]}')
        for d in delegations_data:
            result.append([
                d["account"]["address"],
                v["moniker"],
                d["amount"]["amount"]
            ])
    return result


if __name__ == '__main__':
    data = convert_data()
    df = pd.DataFrame(data, columns=['Source', 'Target', 'Weight'])
    df.to_csv('data/network_delegations.csv', index=False)
