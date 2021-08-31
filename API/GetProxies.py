import requests

class GetProxies():
  def BrazilHttp():
    url = "https://proxy-orbit1.p.rapidapi.com/v1/"
    querystring = {"protocols":"socks4","location":"BR"}
    headers = {
        'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com",
        'x-rapidapi-key': "a3de40893emsh7314f92d8cb6f91p108d25jsna92f85c9682d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

  def UsHttp():
    url = "https://proxy-orbit1.p.rapidapi.com/v1/"
    querystring = {"protocols":"http","location":"US"}
    headers = {
        'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com",
        'x-rapidapi-key': "a3de40893emsh7314f92d8cb6f91p108d25jsna92f85c9682d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response