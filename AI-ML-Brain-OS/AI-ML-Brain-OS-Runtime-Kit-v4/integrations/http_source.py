from brain_os.tools import fetch_url_tool
class HttpSourceAdapter:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = set(allowed_hosts)
    def fetch(self, url):
        return fetch_url_tool(url, allowed_hosts=self.allowed_hosts)
