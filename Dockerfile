FROM timothyjmiller/cloudflare-ddns:latest
WORKDIR /
COPY create_config.py .
CMD python /create_config.py /config.json && python -u /cloudflare-ddns.py --repeat