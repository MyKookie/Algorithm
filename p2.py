import folium
import csv
import random
import numpy as np
from geopy.distance import geodesic
from itertools import product
from itertools import permutations
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def Map_Mark(X):
        m = folium.Map(location=[31.2304, 121.4737], zoom_start=12)
        for i in range(len(X)):


                tooltip = "Click Here For More Info"
                marker = folium.Marker(
                        location=X[i],
                        icon=folium.Icon(icon="cloud"),
                        popup="<stong>starbuck</stong>",
                        tooltip=tooltip)
                marker.add_to(m)


# def get_lowest_sum(X):

#     list_of_distances = [geodesic(a, b).km for a, b in permutations(X, 2)]
#     chunked_list = list()
#     chunk_size = len(X) -1
    
#     for i in range(0,len(list_of_distances),chunk_size):
        
#         chunked_list.append(list_of_distances[i:i+chunk_size])

#     sums =[]
    
#     for i in chunked_list:
        
#         sum = 0.0
        
#         for j in i:
            
#             sum = sum + j
        
#         sums.append(sum)
    
#     coordsindex = sums.index(min(sums))
    
#     return X[coordsindex]


def create_data_model(X):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = X  # yapf: disable
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

# def main(X):
#     """Entry point of the program."""
#     # Instantiate the data problem.
#     data = create_data_model(X)

#     # Create the routing index manager.
#     manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
#                                            data['num_vehicles'], data['depot'])

#     # Create Routing Model.
#     routing = pywrapcp.RoutingModel(manager)


#     transit_callback_index = routing.RegisterTransitCallback(distance_callback)

#     # Define cost of each arc.
#     routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

#     # Setting first solution heuristic.
#     search_parameters = pywrapcp.DefaultRoutingSearchParameters()
#     search_parameters.first_solution_strategy = (
#         routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

#     # Solve the problem.
#     solution = routing.SolveWithParameters(search_parameters)

#     # Print solution on console.
#     if solution:
#         print_solution(manager, routing, solution)
#         folium.PolyLine(points, color='red').add_to(m)


    
file = open('C:/Users/User/hello/Algorithm/starbucks_2018_11_06.csv',encoding="utf8")

csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# # print(header)
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

# print(store_My)
# print("-----------------------------")
# print(store_Cn)
# print("-----------------------------")
# print(store_Jp)
# print("-----------------------------")
# print(store_Kr)
# print("-----------------------------")
# print(store_Mx)
file.close()
#select 6 random store
# s_CN = random.choices(store_Cn, k=6)
# s_MY = random.choices(store_My, k=6)
# s_JP = random.choices(store_Jp, k=6)
# s_KR = random.choices(store_Kr, k=6)
# s_MX = random.choices(store_Mx, k=6)
# X = np.array([
#     ["CN,0"],
#     ["MY,0"],
#     ["JP,0"],
#     ["KR,0"],
#     ["MX,0"],
# ])

s_CN = [['31.260673', '121.499428'], ['31.229257', '121.524293'], ['30.243706', '120.164931'], ['38.91687', '121.635837'], ['39.049373', '121.779125'], ['39.117714', '117.218177']]
s_MY = [['3.814387', '103.327294'], ['3.117951', '101.635792'], ['1.472285', '103.782901'], ['3.202535', '101.733844'], ['3.153336', '101.707138'], ['4.331214', '113.985114']]
s_JP = [['35.881087', '139.827807'], ['33.32841', '130.311539'], ['43.068145', '141.349646'], ['34.661902', '135.081374'], ['35.007649', '135.759842'], ['34.749957', '137.840909']]
s_KR = [['37.39228', '126.95652'], ['35.835315', '128.579907'], ['35.22447', '128.68395'], ['37.48448', '126.8945'], ['35.15968', '129.15951'], ['37.517172', '126.903269']]
s_MX = [['20.679404', '-103.399749'], ['19.41231', '-99.17339'], ['25.72613', '-100.21448'], ['20.66601', '-103.40615'], ['19.55919', '-99.29715'], ['20.69926', '-103.38573']]
s_all = s_CN + s_MY + s_JP + s_KR + s_MX
arr_all = [s_CN, s_MY,s_JP,s_KR,s_MX]
d_cn =[]
d_my =[]
d_jp =[]
d_kr =[]
d_mx =[]
global dist_arr 
dist_arr = [0,0,0,0,0] 
j=0
Y=[[]]
X= np.array([[0],[0],[0],[0],[0]])
#print(s_all)

# m = folium.Map(location=[31.2304, 121.4737], zoom_start=12)
#Map_Mark(s_all)
m = folium.Map(location=[0,0], zoom_start=5)
for i in range(len(s_all)):


    tooltip = "Click Here For More Info"
    marker = folium.Marker(
            location=s_all[i],
            icon=folium.Icon(icon="cloud"),
            popup="<stong>starbuck</stong>",
            tooltip=tooltip)
    marker.add_to(m)

for i in (arr_all):   
    list_of_distances = np.array([int(geodesic(a, b).km) for a, b in product(i, repeat = 2)])
    distance_matrix = list_of_distances.reshape(int(list_of_distances.size**0.5), int(list_of_distances.size**0.5))
    j=j+1
    if j == 1:
        d_cn = distance_matrix
        dist_arr[j-1] = d_cn
    if j == 2:
        d_my= distance_matrix
        dist_arr[j-1] = d_my
    if j == 3:
        d_jp= distance_matrix
        dist_arr[j-1] = d_jp
    if j == 4:
        d_kr= distance_matrix
        dist_arr[j-1] = d_kr
    if j == 5:
        d_mx= distance_matrix
        dist_arr[j-1] = d_mx

 
data = create_data_model(dist_arr[0])
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),data['num_vehicles'], data['depot'] )
routing = pywrapcp.RoutingModel(manager)
transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
solution = routing.SolveWithParameters(search_parameters)
if solution:
    print_solution(manager, routing, solution)
    X[0]= solution.ObjectiveValue()
route = get_route(solution, routing, manager)
m.save('p22.html')



    




