from dataclasses import dataclass
from urllib.request import Request, urlopen
from urllib.parse import urlparse

@dataclass
class ToolResult:
    ok: bool
    data: object = None
    error: str | None = None

class ToolRegistry:
    def __init__(self):
        self._tools = {}
    def register(self, name, fn):
        if name in self._tools:
            raise ValueError(f"tool already registered: {name}")
        self._tools[name] = fn
    def get(self, name):
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        return self._tools[name]
    def names(self):
        return sorted(self._tools)

def echo_tool(text=""):
    return ToolResult(True, {"text": text})

def fetch_url_tool(url, timeout_seconds=5, max_bytes=250_000, allowed_hosts=None):
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        return ToolResult(False, error="only_https_urls_allowed")
    if allowed_hosts is None or parsed.hostname not in allowed_hosts:
        return ToolResult(False, error="host_not_allowlisted")
    try:
        req = Request(url, headers={"User-Agent": "BrainOS-Reference/0.4"})
        with urlopen(req, timeout=timeout_seconds) as response:
            raw = response.read(max_bytes + 1)
            if len(raw) > max_bytes:
                return ToolResult(False, error="response_too_large")
            return ToolResult(True, {"url": response.geturl(), "status": response.status,
                "content_type": response.headers.get("Content-Type", ""),
                "body": raw.decode("utf-8", errors="replace")})
    except Exception as exc:
        return ToolResult(False, error=f"fetch_failed:{type(exc).__name__}")
