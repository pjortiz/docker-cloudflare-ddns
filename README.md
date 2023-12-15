# docker-cloudflare-ddns

Custom Docker Compose configuration for cloudflare-ddns

## Base Image timothymiller/cloudflare-ddns

[:link: GitHub](https://github.com/timothymiller/cloudflare-ddns)

[🐳DockerHub](https://hub.docker.com/r/timothyjmiller/cloudflare-ddns)

## Sample docker-compose.yml

```yaml
version: '3.9'
services:
  cloudflare-ddns:
    image: cloudflare-ddns:latest
    container_name: cloudflare-ddns
    security_opt:
      - no-new-privileges:true
    network_mode: 'host'
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - CLOUDFLARE_CONFIG_IPV4_ENABLED=true
      - CLOUDFLARE_CONFIG_IPV6_ENABLED=false
      - CLOUDFLARE_CONFIG_PURGEUNKNOWNRECORD=false
      - CLOUDFLARE_CONFIG_TTL=301
      - CLOUDFLARE_CONFIG_ZONE_0_ZONEID=9011e7123456789012345678925124e
      - CLOUDFLARE_CONFIG_ZONE_0_AUTHENTICATION_APITOKEN=1234567890abcdef1234567890
      - CLOUDFLARE_CONFIG_ZONE_0_AUTHENTICATION_APIKEY=0987654321abcdef0987654321
      - CLOUDFLARE_CONFIG_ZONE_0_AUTHENTICATION_ACCOUNTEMAIL=user@example_com
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_0_NAME=
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_0_PROXIED=true
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_1_NAME=foo
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_1_PROXIED=true
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_2_NAME=bar
      - CLOUDFLARE_CONFIG_ZONE_0_SUBDOMAIN_2_PROXIED=true
      - CLOUDFLARE_CONFIG_ZONE_1_ZONEID=9011e7123456789012345678925124e22222
      - CLOUDFLARE_CONFIG_ZONE_1_AUTHENTICATION_APITOKEN=1234567890abcdef1234567890
      - CLOUDFLARE_CONFIG_ZONE_1_AUTHENTICATION_APIKEY=0987654321abcdef0987654321
      - CLOUDFLARE_CONFIG_ZONE_1_AUTHENTICATION_ACCOUNTEMAIL=user2@example_com
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_0_NAME=
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_0_PROXIED=false
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_1_NAME=foo2
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_1_PROXIED=false
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_2_NAME=bar2
      - CLOUDFLARE_CONFIG_ZONE_1_SUBDOMAIN_2_PROXIED=false
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
```
