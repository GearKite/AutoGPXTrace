import gpxpy
import gpxpy.gpx
import os

## Set minimum requirements here

requirements = {
    "good_points": -1, # HDOP <= 1
    "bad_points": -1, # HDOP > 1
    "total_points": 100,
    "length": 250, # meters
    "total_moving_time": 100, # seconds
    "average_speed": 0.5, # meters per second
    "accuracy_score": 15 # (good_points) / (bad_points - 2)
}




for filename in os.listdir("input"):
    
    gpx_file = open(f'input/{filename}', 'r')

    gpx = gpxpy.parse(gpx_file)

    total_points = 0
    good_points = 0
    bad_points = 0
    accuracies = []
    length = 0
    moving_data = []
    
    for track in gpx.tracks:
        moving_data.append(track.get_moving_data())
        
        for segment in track.segments:
            length += segment.length_2d() or 0
            for point in segment.points:
                total_points += 1
                if point.horizontal_dilution is None:
                    continue
                elif point.horizontal_dilution > 1:
                    bad_points += 1
                else:
                    good_points += 1
                accuracies = [point.horizontal_dilution]
    
    total_moving_time = 0
    for data in moving_data:
        total_moving_time += data[0]
    
    if total_moving_time > 0:
        # Speed (m/s) = length (meters) / total_moving_time (seconds)
        average_speed = length / total_moving_time
    else:
        average_speed = 0
        
    if bad_points - 2 > 0:
        accuracy_score = (good_points) / (bad_points - 2)
    else:
        accuracy_score = 10000
    
    track_statistics = {
        "good_points": good_points,
        "bad_points": bad_points,
        "total_points": total_points,
        "length": length,
        "total_moving_time": total_moving_time,
        "average_speed": average_speed,
        "accuracy_score": accuracy_score
    }
    
    requirements_not_met = []
    for key, value in track_statistics.items():
        if key not in requirements:
            continue
        if value < requirements[key]:
            requirements_not_met.append((key, value))
            continue
        
        
    if len(requirements_not_met) > 0:
        print(f"Denied {filename}: {requirements_not_met}")
        continue
    
    print(f"Accepted {filename}: {track_statistics}")
    os.rename(f"input/{filename}", f"output/{filename}")
    
    
