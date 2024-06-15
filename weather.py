from random import randrange

class Weather:
    def __init__(self):
        self.wind = None
        self.temp = None

    def sky_conditions(self):
        skyes = ["Sunny", "Partial clouds", "Cloudy", "Dark clouds", "Rain", "Heavy rain", "Thunderstorm"]
        sky_idx = randrange(0, len(skyes))
        sky = skyes[sky_idx]
        wind_dir, speed = self.set_wind(sky)
        temp = self.set_temp(sky)
        return f"Weather conditions: {sky}\nWind speed: {speed} kmh\nWind direction: {wind_dir}\nTemp: {temp}°"
    
    def set_wind(self, sky):
        wind_direction = ["North", "East", "West", "South"]
        rand_idx = randrange(0, len(wind_direction))
        direction = wind_direction[rand_idx]
        wind_speed = 0
        if sky == "Sunny":
            wind_speed = randrange(2, 12)
        elif sky == "Partial clouds":
            wind_speed = randrange(4, 15)
        elif sky == "Cloudy":
            wind_speed = randrange(4, 30)
        elif sky == "Dark clouds":
            wind_speed = randrange(5, 40)
        elif sky == "Rain":
            wind_speed = randrange(5, 50)
        else:
            wind_speed = randrange(10, 120)
        return direction, wind_speed
    
    def set_temp(self, sky):
        
        if sky == "Sunny":
            return randrange(18, 40)
        elif sky == "Cloudy":
            return randrange(10, 20)
        elif sky == "Heavy rain":
            return randrange(8, 15)
        elif sky == "Thunderstorm":
            return randrange(4, 10)
        else:
            return randrange(12, 28)
