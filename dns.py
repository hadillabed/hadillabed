import socket
def get_domain_name(api):
    try:
        domain=socket.gethostbyaddr(api)[0]
        return domain
    except socket.herror:
        return None
api=input("enter api : ")
domain=get_domain_name(api)
if domain: #if domain!= None:
    print(f"the domain of api {api} is {domain}")
else:
    print(f"there is no domain for {api}")