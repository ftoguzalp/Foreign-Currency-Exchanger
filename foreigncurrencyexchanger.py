import requests

url = 'https://api.exchangerate.host/latest'

response = requests.get(url)
data = response.json()


x=input("What is your currency ?:")
y=input("Which currency do you want ?: ")
z=float(input("How much money you want to convert ?: "))

currency1 =data["rates"][x] 
currency2 =data["rates"][y]

print(f"1 {x} = {currency1} euros")
print(f"1 {y} = {currency2} euros")

if currency2 > currency1 :
    print(f"Your money is {z*(currency1*currency2)} {y}.")
elif currency1 > currency2 : 
    print(f"Your money is {z*(currency2/currency1)} {y}.")






