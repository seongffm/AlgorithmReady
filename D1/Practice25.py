#연산자5
salt_water = 100
salt_percent = 20
salt = salt_percent*salt_water/100
water = 200
total_mixture = salt_water + water
mix_water_salt_percent = (salt/total_mixture)*100
print(f"혼합된 소금물의 농도: {mix_water_salt_percent:.2f}%")