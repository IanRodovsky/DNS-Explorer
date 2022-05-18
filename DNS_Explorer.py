# Requires dnspython package installed.

import dns
import dns.resolver
import socket


def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except socket.error:
        return []
    return [result[0]] + result[1]


def dns_request(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for ans in result:
                print(ans)
                print(f'Domain Names: {reverse_dns(ans.to_text())}')
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return


def subdomain_search(domain, dictionary, nums):
    for word in dictionary:
        subdomain = f'{word}.{domain}'
        dns_request(subdomain)
        if nums:
            for i in range(10):
                s = f'{word}{str(i)}.{domain}'
                dns_request(s)


domain = 'google.com'
d = 'subdomains.txt'
with open(d, 'r') as file:
    dictionary = file.read().splitlines()
subdomain_search(domain, dictionary, True)
