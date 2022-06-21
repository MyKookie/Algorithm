from sys import breakpointhook
import folium
import csv
import random
import numpy as np
from geopy.distance import geodesic
from itertools import product
from itertools import permutations
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def get_centre(X):

    list_of_distances = [geodesic(a, b).km for a, b in permutations(X, 2)]
    chunked_list = list()
    chunk_size = len(X) -1
    
    for i in range(0,len(list_of_distances),chunk_size):
        
        chunked_list.append(list_of_distances[i:i+chunk_size])

    sums =[]
    
    for i in chunked_list:
        
        sum = 0.0
        
        for j in i:
            
            sum = sum + j
        
        sums.append(sum)
    
    coordsindex = sums.index(min(sums))
    
    return X[coordsindex]


def create_data_model(X):
    """Stores the data for the problem."""
    list_of_distances = np.array([int(geodesic(a, b).km) for a, b in product(X, repeat = 2)])
    distance_matrix = list_of_distances.reshape(int(list_of_distances.size**0.5), int(list_of_distances.size**0.5))
    data = {}
    data['distance_matrix'] = distance_matrix # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    # print (data)
    return data

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)
    

def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

def get_route(solution, routing, manager):

    #get vehicle route and store it in a one dimensional array 
    #how 'route' looks like: [0, 7, 2, 3, 4, 6, 8, 1, 5, 9, 0] 
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
      index = solution.Value(routing.NextVar(index))
      route.append(manager.IndexToNode(index))
    routes.append(route)
    return route


    
file = open('C:/Users/User/hello/Algorithm/starbucks_2018_11_06.csv',encoding="utf8")

csvreader = csv.reader(file)
store_Cn=[]
store_My=[]
store_Jp=[]
store_Kr=[]
store_Mx=[]
for row in csvreader:
    location=[]
    if (row[4]== "CN"):
        location.append(row[15])
        location.append(row[16])
        store_Cn.append(location)
    elif (row[4]== "MY"):
        location.append(row[15])
        location.append(row[16])
        store_My.append(location)
    elif (row[4]== "JP"):
        location.append(row[15])
        location.append(row[16])
        store_Jp.append(location)
    elif (row[4]== "KR"):
        location.append(row[15])
        location.append(row[16])
        store_Kr.append(location)
    elif (row[4]== "MX"):
        location.append(row[15])
        location.append(row[16])
        store_Mx.append(location)

file.close()
#select 6 random store
s_CN = random.choices(store_Cn, k=6)
s_MY = random.choices(store_My, k=6)
s_JP = random.choices(store_Jp, k=6)
s_KR = random.choices(store_Kr, k=6)
s_MX = random.choices(store_Mx, k=6)
X = np.array([
    ["CN",0],
    ["MY",0],
    ["JP",0],
    ["KR",0],
    ["MX",0],
])

arr_all = [s_CN, s_MY,s_JP,s_KR,s_MX]
for a in (arr_all):
    c_country=[[float(y) for y in x] for x in a]
    centre = get_centre(c_country)
    index = c_country.index(centre)
    c_country[0],c_country[index] = c_country[index],c_country[0]

            

country_name = ["CN","MY","JP","KR","MX"]

m = folium.Map(location=[0,0], zoom_start=5)
o = 0
p = 0
for i in (arr_all):
    s_country=[[float(y) for y in x] for x in i]
    k=0
    for j in i:
        tooltip = "Click Here For More Info"
        if k == 0:
            marker = folium.Marker(
                location=j,
                icon=folium.Icon(color='red',icon="cloud"),
                popup="{}.{}".format(k,country_name[o]),
                tooltip=tooltip)
            marker.add_to(m)
        else:
            marker = folium.Marker(
                location=j,
                icon=folium.Icon(icon="cloud"),
                popup="{}.{}".format(k,country_name[o]),
                tooltip=tooltip)
            marker.add_to(m)
        k=k+1
    o=o+1
    data = create_data_model(i)
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),data['num_vehicles'], data['depot'] )
    routing = pywrapcp.RoutingModel(manager)
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print(X[p][0])
        print_solution(manager, routing, solution)
        for l in X:
            X[p][1]=solution.ObjectiveValue()
    p=p+1          
    route = get_route(solution, routing, manager)

    for index in range(1, len(route)):
        folium.PolyLine(locations=[s_country[route[index]], s_country[route[index-1]]]).add_to(m)

print(X)
m.save('map.html')
