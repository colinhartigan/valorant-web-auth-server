from valclient import Client

def join_party(username,password,region,party_id):
    client = Client(region=region,auth={'username':username,'password':password})
    client.activate()
    print(client.party_join(party_id))
    return client.party_join(party_id)    