import csv
import datetime as dt

input_filename = 'initial_output.csv'
output_filename = 'data.csv'

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
          'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
          'November': 11, 'December': 12}

input_file = open(input_filename, 'r', encoding='UTF-8', newline='')
output_file = open(output_filename, 'w', encoding='UTF-8')

#read first line first
columns = input_file.readline().strip()
output_file.write('groupchat,' + columns + '\n')

csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')

for line in csv_reader:
    # thread, names, sender, time, text
    thread = line[0]
    partners = line[1]
    sender = line[2]
    text = line[4]

    is_groupchat = ',' in line[1]

    # Saturday, 16 May 2015 at 17:07 UTC+03
    date = line[3].strip().replace('.', '').split(' ')
    
    day = int(date[1])
    month = months[date[2]]
    year = int(date[3])
    
    time = date[5].split(':')
    hour = int(time[0])
    minute = int(time[1])

    timestamp = dt.datetime(year, month, day, hour=hour,
                            minute=minute)
    timestamp = int(timestamp.timestamp())
    

    output_file.write(str(is_groupchat) + ',' +
                      '"' + thread + '",' + 
                      '"' + partners + '",' + 
                      sender + ',' + 
                      str(timestamp) + ',' + 
                      '"' + text + '"\n')

input_file.close()
output_file.close()
