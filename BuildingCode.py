import skyscrapers

skyscraper_raw = skyscrapers.get_skyscraper()
buildings = []
heights = []

for skyscraper in skyscraper_raw:
    buildings.append(skyscraper['name'].lower())
    heights.append(round(skyscraper['statistics']['height']*3.280839895))

def search(buildingInput):
    index = 0
    for b in buildings:
        if b == buildingInput:
            print("The building:", buildingInput, "is", heights[index], "feet tall")
            return heights[index]
        index += 1
    print("The building", buildingInput, "has not been found, try again.")
    return None
buildingInput = input("Building name: ").strip().lower()
search(buildingInput)
