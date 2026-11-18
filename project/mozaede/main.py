







from auction import *
from products import *
def final():
    users=[]

    for i in range(6):
        name=input("name:").strip().upper()
        """kode_meli=input("kode meli:")
        if len(kode_meli)<10 or kode_meli==False:
            print("kode meli irad darad dobare vared kon")
        else:"""
        user = sign_in(name, """kode_meli""")
        users.append(user)
    mahsole()
    print(users)
    r=random.choice(l_product)
    asyncio.run(auction(users,r))