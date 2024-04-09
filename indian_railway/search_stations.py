import requests

url = "https://irctc1.p.rapidapi.com/api/v1/searchStation"

querystring = {"query":"BJU"}

headers = {
	"X-RapidAPI-Key": "89cdfae793mshc05caf30a94ea74p1af4b7jsn6ed674276c6e",
	"X-RapidAPI-Host": "irctc1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())