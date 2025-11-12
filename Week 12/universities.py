import requests
import json
universities_list = {
"Tecmilenio": {
"majors": 24,
"average_semester_cost": 25000,
"closest_campus": "Ciudad Juarez",
"distance_km": 280,
},
"UACJ": {
"majors": 37,
"average_semester_cost": 5000,
"closest_campus": "Ciudad Juarez",
"distance_km": 280,
},
"UPN": {
"majors": 64,
"average_semester_cost": 0,
"closest_campus": "Chihuahua",
"distance_km": 326,

},
"URN": {
"majors": 29,
"average_semester_cost": 10000,
"closest_campus": "Juarez",
"distance_km": 290,
},
"Tec de Monterrey": {
"majors": 44,
"average_semester_cost": 160000,
"closest_campus": "Monterrey",
"distance_km": 920,
},
"BYU_Pathway": {
"majors": 30,
"credit_cost": 3000,
"closest_campus": "Online",
"distance_km": 0,
},
"EAC": {
"majors": 140,
"average_semester_cost": 0,
"closest_campus": "Thatcher",
"distance_km": 466,
},
"tec_casas_grandes": {
"majors": 8,
"average_semester_cost": 3000,
"closest_campus": "Casas Grandes",
"distance_km": 27,
},
}
print("1-Local search \n2-Web site search")
search = int(input("Select the type of information:"))
while search == 1:
    print("1-Tecmilenio\n2-UACJ\n3-UPN\n4-URN\n5-Tec de Monterrey\n6-BYU_Pathway\n7-EAC\n8-tec_casas_grandes")
    x = int(input("What university do you want:"))
    if x == 1:
        print(universities_list["Tecmilenio"])
        break
    elif x == 2:
        print(universities_list["UACJ"])
        break
    elif x == 3:
        print(universities_list["UPN"])
        break
    elif x == 4:
        print(universities_list["URN"])
        break
    elif x == 5:
        print(universities_list["Tec de Monterrey"])
        break
    elif x == 6:
        print(universities_list["BYU_Pathway"])
        break
    elif x == 7:
         print(universities_list["EAC"])
         break
    elif x == 8:
        print(universities_list["tec_casas_grandes"])
        break
while search == 2:
        # print("1-Tecmilenio\n2-UACJ\n3-UPN\n4-URN\n5-Tec de Monterrey\n6-BYU_Pathway\n7-EAC\n8-tec_casas_grandes")
        u = input("Enter the name of the university you want:")
        link = "https://raw.githubusercontent.com/Hipo/university-domains-list/refs/heads/master/world_universities_and_domains.json"
        response = requests.get(link)
        data = response.json()
        
        for university in data:
            if u.lower() in university['name']:
                print(json.dumps(university, indent=2))
                
        break

                    
