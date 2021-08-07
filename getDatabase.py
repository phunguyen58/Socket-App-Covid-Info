import json

def readDataGlobal():
    with open("dataGlobal.json") as f_global:
        global_data = json.load(f_global)
    global_info = "Cases: " + str(global_data['cases']) + "\n" + "Deaths: " + str(global_data['deaths']) + "\n" + "Recovered: " + str(global_data['recovered'])
    return global_info

def readDataByCountry(country_name):
    with open("dataAllCountry.json") as f_country:
        all_country_data = json.load(f_country)
    for country in all_country_data:
        if(country_name == country['country']):
            country_info = "Country: "
            country_info += str(country['country']) + "\n"
            country_info += "Cases: "
            country_info += str(country['cases']) + "\n"
            country_info += "Cases today: "
            country_info += str(country['todayCases']) + "\n"
            country_info += "Deaths: "
            country_info += str(country['deaths']) + "\n"
            country_info += "Today deaths: "
            country_info += str(country['todayDeaths']) + "\n"
            country_info += "Recovered: "
            country_info += str(country['recovered']) + "\n"
            country_info += "Active: "
            country_info += str(country['active']) + "\n"
            country_info += "Critical: "
            country_info += str(country['critical']) + "\n"
            country_info += "Cases per one million: "
            country_info += str(country['casesPerOneMillion']) + "\n"
            country_info += "Deaths per one million: "
            country_info += str(country['deathsPerOneMillion']) + "\n"
            country_info += "Total test: "
            country_info += str(country['totalTests']) + "\n"
            country_info += "Test per one million: "
            country_info += str(country['testsPerOneMillion'])
    return country_info

def readDataInVN(province_name):
    with open("dataVN.json") as f_inVN:
        province_data = json.load(f_inVN)
    for province in province_data:
        if province_name == province['nameProvince']:
            province_info = "Province/City: "
            province_info += province['nameProvince'] + "\n"
            province_info += "Cases: "
            province_info += province['cases'] + "\n"
            province_info += "In progress treatment: "
            province_info += province['inProgress'] + "\n"
            province_info += "Another: "
            province_info += province['another'] + "\n"
            province_info += "Recovered: "
            province_info += province['recovered'] + "\n"
            province_info += "Deaths: "
            province_info += province['deaths'] 
    return province_info

        