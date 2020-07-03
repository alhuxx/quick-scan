#!/usr/bin/env python
import sys
import re
import subprocess

target_address = sys.argv[1]
outgoing_interface = sys.argv[2]

masscan_results = subprocess.run(['masscan', '-p1-65535', target_address + '/32', '--rate=800', '-e' + outgoing_interface], capture_output=True)
masscan_results = masscan_results.stdout.decode()
masscan_port_pattern = re.compile(r'Discovered open port (\d+)/')
masscan_port_search = masscan_port_pattern.findall(masscan_results)
masscan_ports = ','.join(masscan_port_search)

nmap_result = subprocess.run(['nmap', '-A', '-p' + masscan_ports, '-T4', target_address], capture_output=True)

if '80' or '443' in masscan_port_search:
    nikto_option = input('Webpage detected, would you like to scan with Nikto?  [y/n]')
    if nikto_option.lower() == 'y':
        nikto_result = subprocess.run(['nikto', '-h', target_address], capture_output=True)
    elif nikto_option.lower() == 'n':
        pass

with open('report.txt', 'w') as file:
    file.write('\n' + '-' * 60 + 'NMAP RESULTS' + '-' * 60 + '\n')
    file.write(nmap_result.stdout.decode())

    if nikto_result:
        file.write('\n' + '-' * 60 + 'NIKTO RESULTS' + '-' * 60 + '\n')
        file.write(nikto_result.stdout.decode())
    else:
        pass

print('\nDONE\nFinal scan report saved as \'report.txt\'')

while True:
    view_report = input('\nWould you like to view the scan report?  [y/n]')
    if view_report.lower() == 'y':
        subprocess.run(['cat', 'report.txt'])
        sys.exit()
    elif view_report.lower() == 'n':
        sys.exit()
    else:
        print('INVALID CHOICE')
