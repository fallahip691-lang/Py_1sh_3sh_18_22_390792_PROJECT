






import random
l_product = []

iphone7 = {
    "iphone 7 mansory": "custom design, golden cover",
    "price": "10000",
    "quantity": "1/5"
}

vertu_cobra = {
    "vertu signature cobra": "luxury phone, diamond cobra design",
    "price": "360000",
    "quantity": "3/8"
}

caviar_iphone = {
    "caviar gold iphone": "custom gold design",
    "price": "50000",
    "quantity": "1/3"
}

bugatti_chiron = {
    "bugatti chiron les legendes du ciel": "limited edition hypercar",
    "price": "3000000",
    "quantity": "7/20"
}

mansory_g63 = {
    "mercedes g63 mansory": "custom body kit, luxury interior",
    "price": "500000",
    "quantity": "2/10"
}

sweptail = {
    "rolls royce sweptail": "one of one bespoke luxury car",
    "price": "13000000",
    "quantity": "1/1"
}

richard_mille = {
    "richard mille rm 056": "sapphire crystal case, luxury watch",
    "price": "2000000",
    "quantity": "2/5"
}

jacob_co = {
    "jacob and co billionaire": "diamond luxury watch",
    "price": "3000000",
    "quantity": "5/18"
}

patek = {
    "patek philippe grandmaster chime": "complicated mechanical watch",
    "price": "2500000",
    "quantity": "1/10"
}

birkin = {
    "hermes birkin himalaya": "rare crocodile leather luxury bag",
    "price": "300000",
    "quantity": "4/20"
}

jordan_dior = {
    "air jordan 1 dior high": "limited edition sneakers",
    "price": "15000",
    "quantity": "1250/8500"
}

nike_mag = {
    "nike mag 2016": "self lacing futuristic sneakers",
    "price": "50000",
    "quantity": "12/89"
}

lv_supreme = {
    "louis vuitton supreme trunk": "limited luxury collaboration",
    "price": "100000",
    "quantity": "3/10"
}

ps5_gold = {
    "golden playstation 5": "custom gold plated console",
    "price": "20000",
    "quantity": "1/5"
}

gameboy_gold = {
    "golden gameboy": "24 karat gold custom console",
    "price": "10000",
    "quantity": "2/5"
}

ap_black_panther = {
    "audemars piguet black panther": "marvel luxury watch",
    "price": "500000",
    "quantity": "125/250"
}

airpods_gold = {
    "golden airpods max": "custom luxury gold design",
    "price": "15000",
    "quantity": "1/10"
}

lamborghini_svj = {
    "lamborghini aventador svj 63": "limited edition supercar",
    "price": "1000000",
    "quantity": "31/63"
}

rolex_caviar = {
    "rolex caviar custom": "custom luxury watch design",
    "price": "100000",
    "quantity": "1/5"
}

jordan_dior_low = {
    "air jordan 1 dior low": "limited edition sneakers",
    "price": "12000",
    "quantity": "2500/4700"
}

l_product.append(iphone7)
l_product.append(vertu_cobra)
l_product.append(caviar_iphone)
l_product.append(bugatti_chiron)
l_product.append(mansory_g63)
l_product.append(sweptail)
l_product.append(richard_mille)
l_product.append(jacob_co)
l_product.append(patek)
l_product.append(birkin)
l_product.append(jordan_dior)
l_product.append(nike_mag)
l_product.append(lv_supreme)
l_product.append(ps5_gold)
l_product.append(gameboy_gold)
l_product.append(ap_black_panther)
l_product.append(airpods_gold)
l_product.append(lamborghini_svj)
l_product.append(rolex_caviar)
l_product.append(jordan_dior_low)


def mahsole():
    r=random.choice(l_product)
    print(r)