



users = []

def sign_in(name,kode_meli):
    
    

    user = {
        "name": name,
        "kode meli": kode_meli
        
    }

    users.append(user)

    print("Sign in successful!")
    print(f"Welcome {name}")

    return user
