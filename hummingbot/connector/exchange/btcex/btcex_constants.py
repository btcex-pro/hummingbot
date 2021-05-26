# A single source of truth for constant variables related to the exchange

# General
EXCHANGE_NAME = "btcex"

# API
REST_API_VERSON = "v1"

REST_URL = "https://api.btcex.{}/api/exchange/"
WSS_URL = "wss://api.btcex.{}/api/exchange/v1/ws"
AUTH_URL = "https://accounts.btcex.{}/token"

# REST API Public Endpoints
PROFILE_URL = f"{REST_URL+REST_API_VERSON}/profile"  # E.g.


# Websocket Private Channels
WS_PRIVATE_CHANNELS = [
    "open_order",
    "order_history",
    "trade_history",
    "balance"
]
