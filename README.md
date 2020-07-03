# quick scan
### Description
A quick and dirty Python 3 script to automate and (hopefully) speed up the scanning process.<br />
This combines the speed of masscan with the power of nmap to quickly find and scan ports.

### Dependencies
To run successfully, you’ll need to ensure the following are installed:
* masscan
* nmap
* nikto

**Note:** There appears to be a known issue where masscan never returns when running via vpn/tunnel on Debian-based distros, quick scan will therefore run infinitely if this issue is encountered.

### Usage
  To use, simply specify a target IP address as well as an outgoing interface. For example:
  <br />`python3 quick_scan.py 10.10.10.1 eth0`

### Disclaimer
  I take no responsibility for any damage caused when running this script and strongly recommend against its use outside of controlled environments.
