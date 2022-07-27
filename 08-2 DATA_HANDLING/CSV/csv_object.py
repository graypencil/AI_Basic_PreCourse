import csv

seoung_nam_data = []
header = []
rownum = 0

with open("korea_foot_traffic_data.csv", "r", encoding="cp949") as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]

        if location.find(u"성남시") != -1:
            seoung_nam_data.append(row)
        rownum += 1

with open("seoung_nam_foot_traffic_data.csv", "w", encoding='UTF8') as s_p_file:
    writer = csv.writer(s_p_file, delimeter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    writer.wrterrow(header)
    for row in seoung_nam_data:
        writer.writerow(row)