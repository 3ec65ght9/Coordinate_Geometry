import pandas

all_midpoint = ["x1", "x2", "y1", "y2"]
all_gradient = ["y2", "y1", "x2", "x1"]
all_distance = ["y2", "y1", "x2", "x1"]

coordinates_geometry_dict = {
    'midpoint': all_midpoint,
    'gradient': all_gradient,
    'distance': all_distance,
}

coordinates_geometry = pandas.DataFrame(coordinates_geometry_dict)