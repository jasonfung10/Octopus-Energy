import requests
import pandas as pd

def GetUnitRate(this_month, next_month):
    APIKEY = "sk_live_XpSHw3CSxvSBbVidBlTC5Dh8"
    url = f"https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-E/standard-unit-rates/?period_from=2024-{this_month}-01T00:00Z&period_to=2024-{next_month}-01T00:00Z&page_size=1500"
    r = requests.get(url=url, auth=(APIKEY,''))
    output_dict = r.json()
    a = output_dict["results"]

    time =  [each30["valid_from"] for each30 in a]
    unitrate = [each30["value_inc_vat"]for each30 in a]

    data = {
        "time": time,
        "unitrate" : unitrate
    }

    df = pd.DataFrame(data)
    path = f"/Users/jasonfung/Documents/SQL Data Project/Octopus Data/{this_month}_unit_rate.csv"
    df.to_csv(path, index=False)



if __name__ == "__main__":
    this_month = int(input ("Please enter month: "))
    next_month = this_month + 1
    this_month = "{:02d}".format(this_month)
    next_month = "{:02d}".format(next_month)
    GetUnitRate(this_month, next_month)