from datetime import date


tday = date.today()

formatted_tday = tday.strftime("%Y-%m-%d")

print(f"today's date in YYYY-MM-DD format: {formatted_tday}")