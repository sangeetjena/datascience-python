"""Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock."""



s = '12:40:22AM'

tm = ''
x= s[0:8].split(':')
if s.find('PM') != -1:
    if int(x[0]) == 12:
        tm = x[ 0 ] + ':' + x[ 1 ] + ':' + x[ 2 ]
    else:
        tm =str(int(x[0])+12)+':' + x[1]+':'+x[2]
else:
    if int(x[ 0 ]) == 12:
        tm = '00' + ':' + x[ 1 ] + ':' + x[ 2 ]
    else:
        tm = x[ 0 ] + ':' + x[ 1 ] + ':' + x[ 2 ]
print(tm)
