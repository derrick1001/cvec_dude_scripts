#!/usr/bin/python3

from warnings import filterwarnings
from requests import get
from sys import argv, path

path.append('/home/derrick/Derrick-shell-scripts/python/modules')
filterwarnings("ignore", message="Unverified HTTPS request")


def get_ont():
    from crayon import c_BLUE, c_YELLOW, c_CYAN, c_GREEN, c_MAGENTA, c_WHITE
    shelf = (input(f'{c_BLUE}Shelf: {c_WHITE}'))
    slot = (input(f'{c_BLUE}Slot: {c_WHITE}'))
    port = (input(f'{c_BLUE}Port: {c_WHITE}'))
    response = get(f'https://10.20.7.10:18443/rest/v1/performance/device/{argv[1]}/ponstatus/shelf/{shelf}/slot/{slot}/port/{port}/status?refresh=false',
                        auth=('admin', 'Thesearethetimes!'), verify=False)
    r = response.json()
    for i in r:
        ont_id = i.get('ont-id')
        sn = i.get('status').get('serial-number')
        dn_rx = i.get('detail').get('opt-signal-level')
        up_rx = i.get('detail').get('ne-opt-signal-level')
        up_ber = i.get('detail').get('us-sdber-rate')
        dn_ber = i.get('detail').get('ds-sdber-rate')
        rr = i.get('detail').get('latest-restart-reason')
        print(f'\n{c_BLUE}ONT: {c_GREEN}{ont_id}\n{c_BLUE}SN: {c_CYAN}CXNK{sn}\n{c_BLUE}Light U/D: {c_YELLOW}{up_rx}{c_GREEN}/{c_YELLOW}{dn_rx}\n{c_BLUE}BER: {c_YELLOW}{up_ber}{c_GREEN}/{c_YELLOW}{dn_ber}\n{c_MAGENTA}{rr}\n')
    q = input(f'{c_CYAN}Press enter to exit...')
    if q is None:
        exit()


get_ont()
