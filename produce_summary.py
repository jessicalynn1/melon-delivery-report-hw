# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

def daily_summary():
    
    while True:
        
        day_num = 1
        start_date = 19

        if day_num > 3:
            break

        else:
            print(f"Day {day_num}")
            the_file = open(f"um-deliveries-201405{start_date}.txt")
            for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                melon = words[0]
                count = words[1]
                amount = words[2]

                print(f"Delivered {count} {melon}s for total of ${amount}")
                the_file.close()

        day_num = day_num + 1
        start_date = start_date + 1


daily_summary()