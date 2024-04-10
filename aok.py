import sys
import json
import datetime

# analyze YT watch history and print out results 
#
# arg1: watch history dictionary
# arg2: true if you want to take into account YT Shorts when analyzing
#       false if otherwise
def analyze(history, incl_shorts):
    # total videos watched
    total = 0
    # dict for storing # of videos per year
    year_counts = {}
    # current year
    curr_year = datetime.datetime.now().year

    # initiliaze each year to 0
    for temp_year in range(2005, curr_year + 1):
        year_counts[temp_year] = 0

    for item in history:
        # if item has a valid URL and is not YT Music, add it to the count
        # of the year it's listed in
        if 'titleUrl' in item and (item['titleUrl'][8:13] != 'music'):
            year_counts[int(item['time'][0:4])] += 1
            total += 1

    print('============ RESULTS ===========')

    start = False

    for year in year_counts:
        # start printing results from the first non-empty year
        if year_counts[year] != 0:
            start = True

        if start:
            # print [year]: [count]
            # if include YT Shorts is enabled, show a tag next to 2020
            print('%s: %d%s' % (year, year_counts[year], '  [YT Shorts created]' if incl_shorts and year == 2020 else ''))

            if incl_shorts and int(year) >= 2020:
                # on average, about a 14:1 shorts to video ratio
                # est. #non-short videos watched = total * 0.071
                print('  - est. #non-shorts: ', round(year_counts[year] * 0.071))

    # average YT video length is 11.7 minutes
    # est. total time watched = total * 11.7
    total_time = total * 11.7
    # est. total # non-short videos watched
    ns_total = round(total * 0.071)
    # est. total non-short video time watched
    ns_total_time = round(ns_total * 11.7)

    print('================================')
    print('TOTAL: ', total)

    if incl_shorts:
        print('est. non-short TOTAL: ', ns_total)
        print('est. time watched: ', ns_total_time)
        print(' ~%d hrs' % (round(ns_total_time / 60)))
    else:
        print('est time watched: %d min' % (total_time))
        print(' ~%d hrs' %  (round(total_time / 60)))



if len(sys.argv) > 1:
    # open file provided in first command line argument
    # should be a .json file
    with open(sys.argv[1], encoding='utf8') as file:
        # load file as JSON
        history = json.load(file)
        # analyze watch history JSON
        analyze(history, len(sys.argv) > 2 and (sys.argv[2] == '-s' or sys.argv[2] == '--shorts'))
else:
    print('No file provided')
