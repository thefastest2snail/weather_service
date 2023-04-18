import requests
import json
import time
import win32serviceutil
import win32service
import win32event

api_key = 'c3ab4ca3caa15ad0c63c0887fd492f49'

city = 'Almaty'
country_code = 'KZ'
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}')

if response.status_code == 200:
    data = str(response.json())
    json_data = data.replace("\'", "\"")
    weather_data = json.loads(json_data)
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    country_code = weather_data['sys']['country']

    print(f"The temperature in {weather_data['name']}, {country_code} is {int(temperature - 273.15)}°C.")
    print(f"The weather is {description}.")
else:
    print('Error:', response.status_code)


import time
import win32serviceutil
import win32service
import win32event

# class HelloWorldService(win32serviceutil.ServiceFramework):
#     _svc_name_ = "HelloWorldService"
#     _svc_display_name_ = "Hello World Service"
#     _svc_description_ = "A simple Windows service that prints 'Hello, world!' to the console every 10 seconds."

#     def __init__(self, args):
#         win32serviceutil.ServiceFramework.__init__(self, args)
#         self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

#     def SvcStop(self):
#         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
#         win32event.SetEvent(self.hWaitStop)

#     def SvcDoRun(self):
#         while True:
#             print("Hello, world!")
#             time.sleep(10)

# if __name__ == '__main__':
#     win32serviceutil.HandleCommandLine(HelloWorldService)
