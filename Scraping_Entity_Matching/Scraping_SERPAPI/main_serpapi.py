from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import json
import csv
import pandas as pd
# import time

# def write_to_xlsx(save_local_results, filename_excel):
#     print('write to excel...')
#     cols = ['Place name', 'Place type', 'address', 'gps_coordinates', 'website', 'types', 'phone',
#                       'user_review', 'latitude', 'longitude']
#     df = pd.DataFrame(save_local_results, columns=cols)
#     df.to_excel('Pork_farm/belfast.xlsx')


def write_to_csv(save_local_results, filename_csv):
    print('write to csv...')
    path_to_csv = "serpapi_csv_postcode_Organic_Farms/" + filename_csv
    with open(path_to_csv, mode='w', encoding='utf8') as csv_file:
        fieldnames = ['Place name', 'Place type', 'address', 'gps_coordinates', 'website', 'types', 'phone',
                      'user_review', 'latitude', 'longitude']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        farm_data = []
        #     for result in results['local_results']:
        for result in save_local_results:
            # place_name = result['title']
            try:
                place_name = result['title']
            except:
                place_name = None
            try:
                place_type = result['type']
            except:
                place_type = None
            try:
                address = result['address']
            except:
                address = None
            try:
                gps_coordinates = result['gps_coordinates']
            except:
                gps_coordinates = None
            try:
                website = result['website']
            except:
                website = None
            try:
                types = result['types']
            except:
                types = None
            try:
                phone = result['phone']
            except:
                phone = None
            try:
                user_review = result['user_review']
            except:
                user_review = None

            try:
                latitude = result['gps_coordinates']["latitude"]
            except:
                latitude = None

            try:
                longitude = result['gps_coordinates']["longitude"]
            except:
                longitude = None

            farm_data.append({
                'Place name': place_name,
                'Place type': place_type,
                'address': address,
                'gps_coordinates': gps_coordinates,
                'website': website,
                'types': types,
                'phone': phone,
                'user_review': user_review,
                'latitude': latitude,
                'longitude': longitude
            })

        for data in farm_data:
            writer.writerow(data)


def serpapi_pages(query, filename_json):
    params = {
        "api_key":"YOUR API KEY", # API Key
        "engine": "google_maps",
        "type": "search",
        "google_domain": "google.co.uk",
        "q": query,
        "ll": "@40.7455096,-74.0083012,14z",
        "hl": "en",
        "gl": "uk"
    }

    search = GoogleSearch(params)  # where data extraction happens on the backend
    print("start")
    local_results = []

    # pagination
    while True:
        results = search.get_dict()  # JSON -> Python dict
        #     print(results)
        # title = results['local_results']['title']

        if 'next' in results.get('serpapi_pagination', {}):
            search.params_dict.update(
                dict(parse_qsl(urlsplit(results.get('serpapi_pagination', {}).get('next')).query)))
        else:
            break

        local_results.extend(results['local_results'])

    path_to_json = "serpapi_json_postcode_Organic_Farms/" + filename_json
    with open(path_to_json, 'w') as f:
        json.dump(local_results, f)
    # print(json.dumps(local_results, indent=2, ensure_ascii=False))
    print("stop")
    return local_results


def main():
    """ Scrape pages from "input.csv" file and save results to "output.csv" file """

    df_new = pd.read_excel('keyword_postcode_Organic_Farms.xlsx')
    keyword_search = df_new['new_keyword'].to_list()
    count = 1
    for keyword in keyword_search:
        print("keyword is", keyword)
        print(count)
        query = keyword
        filename_csv = "_".join(query.split(" ")) + ".csv"
        # filename_excel = "_".join(query.split(" ")) + ".xlsx"
        filename_json = "_".join(query.split(" ")) + ".json"
        data1 = serpapi_pages(keyword, filename_json)
        # print(data1)
        # write_to_xlsx(data1, filename_csv)
        write_to_csv(data1, filename_csv)
        count += 1
        # time.sleep(3)


if __name__ == "__main__":
    main()
