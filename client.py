from valclient import Client

def join_party(username,password,region,party_id):
    client = Client(region=region,auth={'username':username,'password':password})
    client.activate()
    return client.party_join(party_id)    

def request_party(username,password,region,party_id):
    client = Client(region=region,auth={'username':username,'password':password})
    client.activate()
    return client.party_request(party_id)    