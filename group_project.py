import re 
import requests
import json 
import tkinter as tk
from tkinter import*


api_key = 'AIzaSyAPrM0MRPX0xq7yUuF94oot5EkcKT8iuCc'
def get_address(get_address,place,item):
  #get_address = input('Please enter the address you would like to get delievered to: ' ) 
  separate = re.findall(r'(\d+\s.*)\s(\w+)\s([A-Z]{2})',get_address)
  
  street_info = list(separate[0][0].split(' '))
  house_number = street_info[0]
  street_name = street_info[1]
  street_suffix = street_info[2]
  city_name = separate[0][1]
  state_name = separate[0][2]
  url_get_att = 'https://maps.googleapis.com/maps/api/geocode/json?address='+house_number+street_name+street_suffix+','+city_name+','+state_name+'&key='+api_key
  #print(url_get_att)
  
  
  #------------------------------------------------------------------------
  
  response = requests.get(url_get_att)
  data = json.loads(response.text)
  address_place_id = data['results'][0]['place_id']
  #print(address_place_id)

  get_cords = data['results'][0]['geometry']['location']
  get_lat = get_cords['lat']
  get_lng = get_cords['lng']
  
  #-------------------------------------------------------------------------
  
  type_place = place
  get_item = item
  get_place = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(get_lat)+','+str(get_lng)+'&radius=9500&type='+type_place+'&keyword='+get_item+'&key='+api_key
  
  

  

  response_two = requests.get(get_place)
  data_two = json.loads(response_two.text)
  #print(get_place)
  names = []
  place_ids = []
  for i in data_two['results']:
    
    names.append(i['name'])
    
  for x in data_two['results']:
      place_ids.append(x['place_id'])
  #print(names)
  #print(place_ids)
  
  

  root=Tk()
  sizex = 600
  sizey = 400
  posx  = 40
  posy  = 20
  root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
  

  def CurSelet(evt):
      value=str((mylistbox.get(mylistbox.curselection())))
      #print(value)
      new_dict = dict(zip(names, place_ids))
      #print(new_dict)
      
      for x,y in new_dict.items():
          if value == x:
              #print(y)
              url_time_and_distance = 'https://maps.googleapis.com/maps/api/directions/json?origin=place_id:'+y+'&destination=place_id:'+address_place_id+'&key='+api_key
              response_three = requests.get(url_time_and_distance)
              data_three = json.loads(response_three.text)
                
              get_dist = data_three['routes'][0]['legs'][0]['distance']['text']
              get_time = data_three['routes'][0]['legs'][0]['duration']['text']
              
              remove_mi = re.findall(r'\d*[.,]?\d*',get_dist)
              get_mi = remove_mi[0]
              pass_str = float(get_mi)
            
              fuelCharge = pass_str * 0.8
              price = 4.5 + fuelCharge
      
              print('Price: ',price)
              print(get_time)

  mylistbox=Listbox(root,width=60,height=10,font=('times',13))
  mylistbox.bind('<<ListboxSelect>>',CurSelet)
  mylistbox.place(x=32,y=90)

  for items in names:
    mylistbox.insert(END,items)
  root.mainloop()
  
  



if __name__ == "__main__":
    
  get_address(get_address,get_address,get_address)
    
  