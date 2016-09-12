from craigslist import CraigslistHousing

BOXES = {
    "redwood_city": [
       [-122.288383,37.447636],
       [-122.139771,37.569534]
    ],
    "menlo_park+palo_alto": [
	[-122.229118,37.41692],[-122.081696,37.534336]
    ],
    "mountain_view+santa_clara+sunnyvale": [
       [-122.168999,37.332085],[-121.914253,37.425934]
    ]

}
NEIGHBORHOODS = ['menlo park', 'mountain view', 'palo alto', 'sunnyvale', 'santa clara', 'los altos', 'redwood city']

cl = CraigslistHousing(site='sfbay', area='sfc', category='apa',
                         filters={'max_price': 2000, 'min_price': 1000})

def in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

results = cl.get_results(sort_by='newest', geotagged=True, limit=20)
for result in results: 
    geotag = result["geotag"]
    area_found = False
    area = ""
    for a, coords in BOXES.items():
        if in_box(geotag, coords):
            area = a
            area_found = True
    
    location = result["where"]
    for hood in NEIGHBORHOODS:
        if hood in location.lower():
            area = hood
