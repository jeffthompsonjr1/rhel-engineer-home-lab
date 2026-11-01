# Webserver Performance Baseline — 2026-11-01

## Environment
- Server: rhel-webserver-stg
- Operating system: RHEL 9.8
- Web server: Apache HTTP Server
- Applications: Thompson's Lovely Creations and Annie's Paint Lab
- Supporting services: PHP-FPM and MariaDB
- Public domain: thompsonslovelycreations.com

## System Resources

| Metric | Value |
|---|---|
| Total RAM | 1.6 GiB |
| Available RAM | 1.0 GiB |
| Swap used | 0 B |
| Apache memory | 29.2 MiB |
| PHP-FPM memory | 21.6 MiB |
| MariaDB memory | 95.5 MiB |
| Website storage | 131 MB |
| Annie's Paint Lab storage | 114 MB |

MariaDB is running without an application database workload.

## HTTP Response Measurements

| Page | Public TTFB | Local TTFB | Status |
|---|---|---|---|
| TLC Home | 220.904 ms | 0.737 ms | 200 |
| TLC About | 149.834 ms | 0.500 ms | 200 |
| Annie's Home | 159.146 ms | 0.648 ms | 200 |
| Annie's Portfolio | 145.171 ms | 1.047 ms | 200 |

Measurements were collected using curl. Public requests traversed Cloudflare; local requests targeted Apache at 127.0.0.1 over HTTP.

## Security Findings

- SEC-001: MariaDB restricted to localhost.
- SEC-002: SSH password authentication and direct root login disabled.
- WEB-SEC-003: Annie's admin.html and lamp_config.txt moved outside the document root; public URLs subsequently returned HTTP 404.
- Webserver package assessment: No available updates reported.

## Limitations

- Single response-time measurement per page.
- No concurrent-user load testing.
- Browser rendering and complete page assets not measured.
- No database workload.
- No long-term CPU, memory, or latency monitoring established.

## Follow-Up Tasks

- Measure complete page loading and image sizes.
- Establish recurring performance monitoring.
- Review remaining publicly accessible files and Apache security settings.
- Establish backup and recovery procedures.
- Deploy a test server for changes before production.
- Review controller security advisories and schedule patching.

