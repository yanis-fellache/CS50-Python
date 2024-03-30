import requests
import sys


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    #print(json.dumps(response, indent=2))
    usd_rate = response["bpi"]["USD"]["rate"].replace(",","")


    usd_rate = float(usd_rate)
    n = float(sys.argv[1])
    price = n * usd_rate

    print(f"${price:,.4f}")

except:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Command-line argument is not a number")
