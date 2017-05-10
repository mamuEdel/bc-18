from urllib.request import urlopen
import json
def get_information():
      API_url='http://restcountries.eu/rest/v2/name/kenya?fullText=true'
      request=urlopen(API_url)
      data=request.read().decode('utf')
      json_obj=json.loads(data)
      
      print (json_obj[0]['capital'])
get_information()