
# Author : GothamPhantom

import dns.resolver
from tqdm import tqdm
import termcolor

print(""" \x1b[38;5;214m
 ██████╗  ██████╗ ████████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔════╝ ██╔═══██╗╚══██╔══╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██║  ███╗██║   ██║   ██║   ███████║███████║██╔████╔██║██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██║   ██║██║   ██║   ██║   ██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
╚██████╔╝╚██████╔╝   ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
		""")

domain = input("[+Phantom Subdo Enum+] Domain name: ")
wordlist_file = input("[+Phantom Subdo Enum+] Wordlist path: ")

print(""" \x1b[38;5;214m
===============================================================
Phantom Subdo Enum v1.0
by GothamPhantom
===============================================================
[*] Url:                    """, domain, """
[*] Wordlist:               """, wordlist_file, """
===============================================================
		""")

# Load wordlist file into list
with open(wordlist_file) as f:
    wordlist = f.read().splitlines()

# Define the DNS servers to use (optional)
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

# Query DNS for subdomains
subdomains = []
for subdomain in tqdm(wordlist, desc="[*] Enumerating phantom subdomains", unit="phantom subdomain"):
    try:
        answers = dns.resolver.resolve(f'{subdomain}.{domain}', 'A')
        for rdata in answers:
            subdomains.append(f'{subdomain}.{domain} -> {rdata.address}')
    except:
        pass

# Print subdomains
print(termcolor.colored((f'\n[+] Nice work, bud! Found {len(subdomains)} subdomains for {domain}:'), 'green'))
for subdomain in subdomains:
    print(subdomain)
