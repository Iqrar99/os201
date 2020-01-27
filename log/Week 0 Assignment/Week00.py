import hashlib

with open('INPUT.TXT','r') as input_txt:
    data = input_txt.read().strip().split('\n')

user_data = data[0].split(' - ')
user_data[1] = hashlib.sha256(user_data[1].encode()).hexdigest()

year_now = ''
year, term = 0, 0
sks_cumulative = 0

with open(f'{user_data[0]} - {user_data[1]}.txt','w') as output_txt:
    for line in data:
        if 'Tahun Ajaran' in line:
            if line.split()[2] != year_now:
                year_now = line.split()[2]
                year += 1
                term = 1
            else:
                term += 1
            sks_cumulative = 0

        elif 'Disetujui' in line:
            course_data = line.strip().split('\t')
            course_code = course_data[1].strip()
            course_grade = course_data[-2].strip()
            sks_now = course_data[5].strip()
            sks_cumulative += int(sks_now)

            output_txt.write(f'{str(year)+str(term)} {course_code} {sks_now} {course_grade:2} {sks_cumulative:2}\n')
