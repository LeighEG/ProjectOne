import urllib.parse
import requests
import os


		                          	                     	
def get_weather_data(city):
	'''
	Accesss metaweather api and extracts data for a user input city
	'''
	main_api = 'https://www.metaweather.com/api/location/search/?'   
	url = main_api + urllib.parse.urlencode({'query': city})     
	json_data = requests.get(url).json()
	'''
	 Exception check for city entered - make sure city is available 
	 in the metaweather api. If not, inform user and ask for another 
	 city or quit.
	'''                             
	try:
		json_city = json_data[0]['title']                                
	except:
		os.system('cls')
		print('City is not available. Please try again.')
		return
	'''
	Extract and format metaweather api data using json
	'''
	json_wid = json_data[0]['woeid']                                
	json_latt_long = json_data[0]['latt_long']                       
	json_lattitude,json_longitude  = json_latt_long.split(',')       
	url = ('https://www.metaweather.com/api/location/' + str(json_wid))
	json_data = requests.get(url).json()                               
	json_state = json_data['parent']['title']                                 
	json_weather = json_data['consolidated_weather'][0]['weather_state_name'] 
	json_high_temp = json_data['consolidated_weather'][0]['max_temp']         
	high_temp_f = int((json_high_temp * 9/5) + 32)                                 
	json_low_temp = json_data['consolidated_weather'][0]['min_temp']          
	low_temp_f = int((json_low_temp * 9/5) + 32)
	'''
	Clear screen in windows and print data from metaweather api
	'''                                  
	os.system('cls')                                                               
	print(json_city + ', ' + json_state)                             
	print()
	print('Today: ' + json_weather)                                  
	print('HIGH: ' + str(high_temp_f))                               
	print('LOW: ' + str(low_temp_f))                                 
	print('Lattitude: ' + json_lattitude)                            
	print('Longitude: ' + json_longitude)
	print('Thank you') 
	
	                                        
  
while True:
	
	response = input('\nEnter city or "quit": ')
	if response != 'quit':
		get_weather_data(response)
	else:
		break	                                                                   
		
			
		
		
		  
		
		                                       
		
			
			
			
			
			
			
