from weather import Weather
from player import Player

def fishing():
    pass


def choose_bait():
    pass


def main():
    print(r'''


    ___      _       _                              _ _ 
   / __\__ _| |_ ___| |__     ___ _ __ ___     __ _| | |
  / /  / _` | __/ __| '_ \   / _ \ '_ ` _ \   / _` | | |
 / /__| (_| | || (__| | | | |  __/ | | | | | | (_| | | |
 \____/\__,_|\__\___|_| |_|  \___|_| |_| |_|  \__,_|_|_|
                                                       
           .----         -                                    
      .-*'`    `*-.._.-''/
     ()  ) * )  ,       (  
      `*-._`._(__.--*"`.\
                       
''')
    print("\nWelcome to Catch em all!\n")
    weather = Weather()
    print(weather.sky_conditions())




if __name__ == "__main__":
    main()