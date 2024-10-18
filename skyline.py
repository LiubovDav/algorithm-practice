# Add your clarifying questions here

def skyline(building_list):
    max_building_height = 0
    result = []

    for i in range(len(building_list) - 1):
        if building_list[i] > max_building_height:
            result.append(building_list[i])
            max_building_height = building_list[i]

    return result

print(skyline([-1, 1, 3, 7, 7, 3]))
