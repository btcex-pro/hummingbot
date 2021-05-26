import aiohttp
from enum import Enum


class HttpMethods(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"


HTTP_REQUESTS = {
    "example": {
        "url": "",
        "method": HttpMethods.GET,
    }
}


class HttpClientFactory():
    client = None

    def __init__(self):
        pass

    @staticmethod
    def getClient(self):
        client = self.client
        if client is None:
            self.client = aiohttp.ClientSession()
            return self.client
        return client


class Request():
    def __init__(self, clientFactory):
        self.clientFactory = clientFactory.getClient


class HttpRequest(Request):
    def __init__(self, client):
        super(client)


class StreamRequest(Request):
    def __init__(self, client):
        super(client)
