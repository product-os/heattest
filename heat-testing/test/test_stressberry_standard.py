import yaml 

# import datetime
# import os
# import http.server
# import socketserver

# PORT=80

# print ("Running stressberry with default inputs...")

# d = datetime.datetime.now()
# filename = d.isoformat().replace(":","-").split(".")[0]+".dat"
# # file will be named something like `2020-01-27T14-08-51.dat`
# return_value = os.system("stressberry-run "+filename)
# print ("Returned value - ", return_value)

# print ("...Done")
# print ("Starting server ...")

# class Handler(http.server.SimpleHTTPRequestHandler):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, directory="./", **kwargs)

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
    
def test_max_core_temp():
    # print("Finding max temp")
    data_file = open("out.dat","r")
    data = yaml.load(data_file, Loader=yaml.SafeLoader) 
    print("Max core temp \t- ",max(data['temperature']))
    print("Average ambient - ",sum(data['ambient'])/len(data['ambient']))
    sum_diff = 0
    for d in range(1, len(data['time'])):
        sum_diff = sum_diff + data['time'][d] - data['time'][d-1]
    print (sum_diff/len(data['time']))
    # print (len(data['cpu frequency']))
    # print (len(data['ambient']))
    # print (len(data['time']))
    # print (len(data['temperature']))

    # Ignore the first and last elements that are not part of the test
    
    # min_index = data['cpu frequency'].index(min(data['cpu frequency'][150:]))
    # print ("Time for min CPU - ",data['time'][min_index])
    # print("Min CPU - ", min(data['cpu frequency']))
    
    # max_index = data['cpu frequency'].index(max(data['cpu frequency'][150:]))
    # print ("Time for max CPU - ",data['time'][max_index])
    # print("Max CPU - ", max(data['cpu frequency']))

    # # Check if the max temperature is less than 80
    # assert max(data['temperature']) < 80


test_max_core_temp()
