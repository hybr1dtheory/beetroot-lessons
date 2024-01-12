"""This module allows you to calculate total losses of russian soldiers and equipment 
over the specified period of time (min date = 2022-02-25, max date - today).
The summary will be downloaded to summary.json file"""
import requests as rq
import json
from datetime import date


def check_dates(df: str, dt: str) -> tuple:
    min_date = date.fromisoformat("2022-02-25")
    max_date = date.today()
    try:
        date_f = date.fromisoformat(df)
    except:
        print("Error! Wrong start date format (right format YYYY-MM-DD. Try again")
        return False, False
    try:
        date_t = date.fromisoformat(dt)
    except:
        print("Error! Wrong final date format (right format YYYY-MM-DD)")
        return df, False
    if date_t < date_f:
        print("Error! Final date cannot be less than start day.")
        return False, False
    elif date_f < min_date:
        print("Error! Start date cannot be less than 2022-02-25.")
        return False, dt
    elif date_t > max_date:
        print(f"Error! Final date cannot be greater than {max_date}.")
        return df, False
    return df, dt


while True:
    print("Please, enter dates in ISO format - YYYY-MM-DD.\
    For example: 7 january 2024 -> 2024-01-07")
    df = input("Enter start date of the period: ").strip()
    dt = input("Enter final date of the period: ").strip()
    date_from, date_to = check_dates(df, dt)
    if date_from and date_to:
        break
    else:
        print("Try again.")


url = f"https://russianwarship.rip/api/v2/statistics?date_from={date_from}&date_to={date_to}"
req = rq.get(url)
if req:
    data = req.json()
    records = data["data"]["records"]
    summary = {}
    for rec in records:
        for k, v in rec["increase"].items():
            summary[k] = summary.get(k, 0) + v
    print(f"\nSummary from {df} to {dt}:")
    for k, v in summary.items():
        print(f"{k.rjust(26)} : {v}")
    result = {"date_from": df, "date_to": dt, "summary": summary}
    with open("summary.json", 'w') as fw:
        json.dump(result, fw, indent=4)
else:
    print("Request error:", req.status_code)
