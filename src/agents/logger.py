import logging

logger = logging.getLogger("openai.agents")

# Show everything the SDK + httpx is sending
logging.basicConfig(level=logging.INFO)

# If you only want httpx (REST/WebSocket payloads)
logging.getLogger("httpx").setLevel(logging.INFO)

# If you also want to see websocket event traffic
logging.getLogger("websockets").setLevel(logging.INFO)
