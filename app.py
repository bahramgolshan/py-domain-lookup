"""
    Module docstring
"""

import whois
import validators


def domain_lookup(dm):
    """
        Function docstring
    """
    if validators.domain(dm):  # Check if Domain is Valid
        try:
            return whois.whois(dm)  # Get Domain Info

            # example output for hackernoon.com
            # {
            # "domain_name": [
            #     "HACKERNOON.COM",
            #     "hackernoon.com"
            # ],
            # "registrar": "GoDaddy.com, LLC",
            # "whois_server": "whois.godaddy.com",
            # "referral_url": null,
            # "updated_date": [
            #     "2022-11-03 15:45:14",
            #     "2022-04-04 12:33:12"
            # ],
            # "creation_date": [
            #     "2016-04-03 23:11:48",
            #     "2016-04-03 18:11:48"
            # ],
            # "expiration_date": [
            #     "2023-04-03 23:11:48",
            #     "2023-04-03 18:11:48"
            # ],
            # "name_servers": [
            #     "AMBER.NS.CLOUDFLARE.COM",
            #     "GUY.NS.CLOUDFLARE.COM"
            # ],
            # "status": [
            #     "clientDeleteProhibited https://icann.org/epp#cliDelProh",
            #     "clientRenewProhibited https://icann.org/epp#cliRenProh",
            #     "clientTransferProhibited https://icann.org/epp#cliTranProh",
            #     "clientUpdateProhibited https://icann.org/epp#cliUpProh"
            # ],
            # "emails": "abuse@godaddy.com",
            # "dnssec": "unsigned",
            # "name": "Registration Private",
            # "org": "Domains By Proxy, LLC",
            # "address": [
            #     "DomainsByProxy.com",
            #     "2155 E Warner Rd"
            # ],
            # "city": "Tempe",
            # "state": "Arizona",
            # "registrant_postal_code": "85284",
            # "country": "US"
            # }

        except ValueError:
            return f"{dm} is not registered"

    else:
        return "Enter a valid domain"


if __name__ == "__main__":

    domain = input("Enter domain:")

    dm_info = domain_lookup(domain)

    print("Registar:", dm_info.registrar)

    print("Creation Date:", dm_info.creation_date)

    print("Expiration Date:", dm_info.expiration_date)

    print("Country:", dm_info.country)
