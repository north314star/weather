import requests



start_over = 'true'
while True:
        city = input('Enter a city name you want to look at:')

        api_key ='dd29fda4360eb6271e53bbe6a6e445ce'

        def get_weather(api_key, city):
         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"

         r = requests.get(url)
         res = r.json()

         temp = res ['main']['temp']
         temp_min = res['main']['temp_min']
         temp_max = res['main']['temp_max'] 
         feels_like = res['main']['feels_like']
         humidity = res ['main']['humidity']
         condition = res['weather'][0]['main']
         description = res['weather'][0]['description']
    

    
    
         print(f"Condition: {condition}\nTemp: {temp}'F\nTemp Max: {temp_max}'F\nTemp Min: {temp_min}'F\nFeels Like: {feels_like}'F\nHumidity: {humidity}%\nDescription: {description}")
         redo_program = input('to restart type y or to quit type Enter')
         if redo_program == 'y':
             start_over = 'true'
         else:
             print('Goodbye')
        
        get_weather(api_key, city)
        
        break



