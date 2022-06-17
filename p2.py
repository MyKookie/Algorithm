import folium
import csv
import random

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
        #m.save('p22.html')

file = open('C:/Users/User/hello/Algorithm/starbucks_2018_11_06.csv',encoding="utf8")

csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)
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


s_CN = [['31.260673', '121.499428'], ['31.229257', '121.524293'], ['30.243706', '120.164931'], ['38.91687', '121.635837'], ['39.049373', '121.779125'], ['39.117714', '117.218177']]
s_MY = [['3.814387', '103.327294'], ['3.117951', '101.635792'], ['1.472285', '103.782901'], ['3.202535', '101.733844'], ['3.153336', '101.707138'], ['4.331214', '113.985114']]
s_JP = [['35.881087', '139.827807'], ['33.32841', '130.311539'], ['43.068145', '141.349646'], ['34.661902', '135.081374'], ['35.007649', '135.759842'], ['34.749957', '137.840909']]
s_KR = [['37.39228', '126.95652'], ['35.835315', '128.579907'], ['35.22447', '128.68395'], ['37.48448', '126.8945'], ['35.15968', '129.15951'], ['37.517172', '126.903269']]
s_MX = [['20.679404', '-103.399749'], ['19.41231', '-99.17339'], ['25.72613', '-100.21448'], ['20.66601', '-103.40615'], ['19.55919', '-99.29715'], ['20.69926', '-103.38573']]
s_all = s_CN + s_MY + s_JP + s_KR + s_MX
print(s_all)

# m = folium.Map(location=[31.2304, 121.4737], zoom_start=12)
Map_Mark(s_all)



