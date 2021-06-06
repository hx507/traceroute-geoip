#!/usr/bin/env python3
import geoip2.database
import geoip2
import sys
if len(sys.argv) != 2:
    print('Usage: python3 lookup.py [ip addr]')
ip = sys.argv[1]
language = 'zh-CN'
try:
    with geoip2.database.Reader('./GeoLite2-City.mmdb') as reader:
        with geoip2.database.Reader('./GeoLite2-ASN.mmdb') as reader2:
            response = reader.city(ip)
            response2 = reader2.asn(ip)
            org = response2.autonomous_system_organization
            city = response.city.name
            country = response.country.names[language]
            subdivition = response.subdivisions.most_specific.name
            network = response.traits.network
            iso_code = response.subdivisions.most_specific.iso_code
            print(
                f'[{city}, {country}{", "+iso_code if iso_code is not None else ""}] {subdivition} {network}')
except geoip2.errors.AddressNotFoundError:
    print('[Not found]')
    pass
