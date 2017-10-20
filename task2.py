from weather import Weather
weather = Weather()

# Lookup via location name.
location = weather.lookup_by_location('halifax')
condition = location.condition()
print (condition['text'])

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
#    print (forecasts['high'])
#    print (forecasts['low'])

  if (forecasts['text']) == 'showers':
    print (forecasts['date'])

