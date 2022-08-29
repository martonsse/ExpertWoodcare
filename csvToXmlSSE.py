#EWC INTELLECTUAL PROPERTY BY MV
#TO USE FORMAT CSV IN FORMAT ON GOOGLE DRIVE
#RENAME INPUT.CSV

#input
import csv
f = open('input.csv')
csv_f = csv.reader(f)
data = []

#csv -> data array
for row in csv_f:
    data.append(row)
f.close()

#output
with open('output.xml', 'w') as e:
    e.write('<?xml version="1.0" encoding="utf-8"?>\n<markers>\n')

    for x in range(len(data)):
        e.write('       <marker name="'+data[x][0]+'" lat="'+data[x][1]+'" lng="'+data[x][2]+'" category="" address="'+data[x][3]+'" address2="" '
                'city="'+data[x][4]+'" state="'+data[x][5]+'" postal="'+data[x][6]+'" country="'+data[x][7]+'" phone="'+data[x][8]+'" email="'+data[x][9]+'" web="'+data[x][10]+'" '
                'hours1="'+data[x][11]+'" hours2="'+data[x][12]+'" hours3="'+data[x][13]+'" featured="" features="" />\n')
    e.write('</markers>')

