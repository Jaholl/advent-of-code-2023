import re, time

start_time = time.time()
lines = open("day1/input.txt", "r").readlines()

def convert_number(numb):
    match numb:
            case 'one'|'eno':
                return '1'
            case 'two'|'owt':
                return '2'
            case 'three'|'eerht':
                return '3'
            case 'four'|'ruof':
                return '4'
            case 'five'|'evif':
                return '5'
            case 'six'|'xis':
                return '6'
            case 'seven'|'neves':
                return '7'
            case 'eight'|'thgie':
                return '8'
            case 'nine'|'enin':
                return '9'
    return numb
        
found_numbers = []
for line in lines:
    match1 = convert_number(re.search("\d|one|two|three|four|five|six|seven|eight|nine", line).group())
    match2 = convert_number(re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1]).group())
    
    found_numbers.append(int(str(match1)+str(match2)))

print(sum(found_numbers))
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))
