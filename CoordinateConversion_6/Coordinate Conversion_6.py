
def dd_to_dms(dd: float, coord_type: str):
    """
    Convert decimal degrees to DMS.
    coord_type: 'lat' or 'lon'
    """
    # קובעים כיוון לפי הסוג והסימן
    if coord_type == "lat":
        direction = "N" if dd >= 0 else "S"
    else:  # lon
        direction = "E" if dd >= 0 else "W"

    dd = abs(dd)

    degrees = int(dd)
    minutes_float = (dd - degrees) * 60
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 2)

    return [degrees, minutes, seconds, direction]



def convert_coordinates(dd_list):
    """
    Convert [lon, lat] or [lon, lat, altitude] to DMS format
    """
    lon = dd_list[0]
    lat = dd_list[1]

    dms = [
        dd_to_dms(lon, "lon"),
        dd_to_dms(lat, "lat")
    ]

    # אם יש גובה – מצרפים אותו כמו שהוא
    if len(dd_list) == 3:
        dms.append(dd_list[2])

    return dms

#ניסיון זימון אחד

los_angeles_dd = [-118.2437, 34.0522]

los_angeles_dms = convert_coordinates(los_angeles_dd)

print(los_angeles_dms)

# ניסיון זימון שני שלי עובד

anchorage_dd = [-149.9002, 61.2181, 22]

anchorage_dms = convert_coordinates(anchorage_dd)

print(anchorage_dms)


# def convert_to_dms(value: float, coord_type: str):
#     """
#     Convert decimal degrees to DMS format.
#     coord_type: 'lat' or 'lon'
#     """
#     direction = ""
#     abs_value = abs(value)

#     degrees = int(abs_value)
#     minutes_float = (abs_value - degrees) * 60
#     minutes = int(minutes_float)
#     seconds = round((minutes_float - minutes) * 60, 2)

#     if coord_type == "lat":
#         direction = "N" if value >= 0 else "S"
#     elif coord_type == "lon":
#         direction = "E" if value >= 0 else "W"

#     return [degrees, minutes, seconds, direction]


# def convert_coordinates(dd):
#     """
#     Convert [longitude, latitude] from DD to DMS
#     """
#     lon, lat = dd
#     return [
#         convert_to_dms(lon, "lon"),
#         convert_to_dms(lat, "lat")
#     ]


# if __name__ == "__main__":
#     anchorage = [-149.9002, 61.2181]
#     los_angeles = [-118.2437, 34.0522]

#     print("Anchorage:", convert_coordinates(anchorage))
#     print("Los Angeles:", convert_coordinates(los_angeles))

