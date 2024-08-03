import requests


def main():
    url = "https://integr8fuels.com/wp-admin/admin-ajax.php"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"macOS"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    params = {
        "action": "getLatestPriceByPortFuels",
        "portId": 2615
    }

    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        data_json = response.json()

        VLSFO, HSFO = None, None
        for price in data_json.get("data", {}).get("prices"):
            fuelGroupName = price.get("fuelGroupName", "")
            if fuelGroupName == "VLSFO":
                VLSFO = price.get("currentPrice", None)
            elif fuelGroupName == "HSFO":
                HSFO = price.get("currentPrice", None)

        print(f"VLSFO: {VLSFO}$")
        print(f"HSFO: {HSFO}$")


if __name__ == "__main__":
    main()