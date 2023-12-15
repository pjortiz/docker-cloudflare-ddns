import json
import os
import sys

def mapAuthorization(authentication: dict, auth_field: str, value: str):
    if auth_field == 'APITOKEN':
        authentication['api_token'] = value
    elif auth_field == 'APIKEY' or auth_field == 'ACCOUNTEMAIL':
        if 'api_key' not in authentication:
            authentication['api_key'] = {}
        if auth_field == 'APIKEY':
            authentication['api_key']['api_key'] = value
        elif auth_field == 'ACCOUNTEMAIL':
            authentication['api_key']['account_email'] = value

def mapZone(zones: dict, key: str, value: str):
    parts = key.split('_')
    zone_index = int(parts[3])
    field = parts[4]

    if zone_index not in zones:
        zones[zone_index] = {}

    if field.startswith('AUTHENTICATION'):
        if 'authentication' not in zones[zone_index]:
            zones[zone_index]['authentication'] = {}
        authentication = zones[zone_index]['authentication']
        auth_field = parts[5]
        mapAuthorization(authentication, auth_field, value)
    elif field == 'ZONEID':
        zones[zone_index]['zone_id'] = value
    elif field.startswith('SUBDOMAIN'):
        sub_index = int(parts[5])
        if 'subdomains' not in zones[zone_index]:
            zones[zone_index]['subdomains'] = []

        while len(zones[zone_index]['subdomains']) <= sub_index:
            zones[zone_index]['subdomains'].append({})

        sub_field = parts[6]
        if sub_field == 'NAME':
            zones[zone_index]['subdomains'][sub_index]['name'] = value
        elif sub_field == 'PROXIED':
            zones[zone_index]['subdomains'][sub_index]['proxied'] = value.lower() == 'true'

def mapBalancer(balancers: dict, key: str, value: str):
    parts = key.split('_')
    balancer_index = int(parts[3])
    field = parts[4]
    
    if balancer_index not in balancers:
        balancers[balancer_index] = {}
    
    if field.startswith('AUTHENTICATION'):
        if 'authentication' not in balancers[balancer_index]:
            balancers[balancer_index]['authentication'] = {}
        authentication = balancers[balancer_index]['authentication']
        auth_field = parts[5]
        mapAuthorization(authentication, auth_field, value)
    elif field == 'POOLID':
        balancers[balancer_index]['pool_id'] = value 
    elif field == 'ORIGIN':
        balancers[balancer_index]['origin'] = value 
    

# Check if the command-line argument for the file location is provided
if len(sys.argv) < 2:
    print("Please provide the file location for saving config.json.")
    sys.exit(1)

file_location = sys.argv[1]

# Initialize the config structure
config = {
    "cloudflare": [],
    "a": os.getenv('CLOUDFLARE_CONFIG_IPV4_ENABLED', 'true').lower() == 'true',
    "aaaa": os.getenv('CLOUDFLARE_CONFIG_IPV6_ENABLED', 'true').lower() == 'true',
    "purgeUnknownRecords": os.getenv('CLOUDFLARE_CONFIG_PURGEUNKNOWNRECORD', 'false').lower() == 'true',
    "ttl": int(os.getenv('CLOUDFLARE_CONFIG_TTL', '300'))
}

zones = {}
balancers = {}
for key, value in os.environ.items():
    # Process zone information 
    if key.startswith('CLOUDFLARE_CONFIG_ZONE_'):
        mapZone(zones, key, value)
    # Process balancer information 
    elif key.startswith('CLOUDFLARE_CONFIG_BALANCER_'):
        mapBalancer(balancers, key, value)



# Add processed zone information to the config
if len(zones.keys()) > 0:
    config['cloudflare'] = list(zones.values())

# Add processed balancer information to the config
if len(balancers.keys()) > 0:
    config['load_balancer'] = list(balancers.values())

# Write the config to the specified JSON file location
with open(file_location, 'w') as file:
    json.dump(config, file, indent=2)

print(f"Config JSON file saved to {file_location}")