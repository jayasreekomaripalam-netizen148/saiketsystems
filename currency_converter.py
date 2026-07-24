import requests


def get_exchange_rate(from_currency, to_currency):

    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url, timeout=10)

        data = response.json()

        if data["result"] == "success":
            rate = data["rates"].get(to_currency)

            if rate:
                return rate
            else:
                print("Currency not available.")
                return None

        else:
            print("Unable to get exchange rates.")
            return None

    except requests.exceptions.RequestException:
        print("Error: Internet connection problem.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def convert_currency():

    print("===== CURRENCY CONVERTER =====")

    try:
        amount = float(input("Enter amount: "))

        from_currency = input(
            "Enter source currency (Example: USD): "
        ).upper()

        to_currency = input(
            "Enter target currency (Example: INR): "
        ).upper()


        rate = get_exchange_rate(
            from_currency,
            to_currency
        )

        if rate:

            converted_amount = amount * rate

            print("\nConversion Result:")
            print(
                f"{amount} {from_currency} = "
                f"{converted_amount:.2f} {to_currency}"
            )

    except ValueError:
        print("Invalid amount. Please enter a number.")


if __name__ == "__main__":
    convert_currency()