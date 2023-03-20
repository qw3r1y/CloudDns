import socket
import dns.resolver


def is_cloud_platform(url):
    try:
        # Resolve the domain name to an IP address
        ip_address = socket.gethostbyname(url)

        # Check if the IP address matches any of the cloud platform IP ranges
        aws_ip_ranges = dns.resolver.query('_netblocks.amazon.com', 'TXT')
        azure_ip_ranges = dns.resolver.query('_cloud-netblocks.microsoft.com', 'TXT')
        gcp_ip_ranges = dns.resolver.query('_cloud-netblocks.googleusercontent.com', 'TXT')

        for ip_range in aws_ip_ranges:
            if ip_address in ip_range.to_text().split():
                return 'Amazon Web Services'
        for ip_range in azure_ip_ranges:
            if ip_address in ip_range.to_text().split():
                return 'Microsoft Azure'
        for ip_range in gcp_ip_ranges:
            if ip_address in ip_range.to_text().split():
                return 'Google Cloud Platform'

        return 'Not a cloud platform'

    except:
        return 'Error resolving DNS'

# Example usage
url = 'https://cloud.google.com/'
platform = is_cloud_platform(url)
print(f'The website at {url} is hosted on {platform}')
