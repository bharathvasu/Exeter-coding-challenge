import time
import tracemalloc
import csv
import re
tracemalloc.start()
try:
    start_time = time.time()
    file_in = open("t8.shakespeare.txt", "r")
    data = file_in.read()
    file_in.close()

    find_list = open("find_words.txt", "r")
    list = find_list.readlines()


    freq = []
    list = [x.strip() for x in list]


    with open('french_dictionary.csv', mode='r') as inp:
        reader = csv.reader(inp)

        dict_from_csv = {rows[0]: rows[1] for rows in reader}

    for word in list:
        w = r"\b{}\b".format(word)

        count = len(re.findall(w, data,re.IGNORECASE))

        data = re.sub(w, dict_from_csv[word], data, flags=re.IGNORECASE)

        freq.append([word, dict_from_csv[word], str(count)])

    file_out = open("t8.shakespeare.translated.txt", "wt", encoding='UTF-8')
    file_out.write(data)
    file_out.close()

    with open("frequency.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['English word', 'French word', 'Frequency'])
        csvwriter.writerows(freq)
    csvfile.close()

    end_time = time.time()
    print("Execution time in seconds",end_time-start_time)
    print("memory usage(current,maximum)",tracemalloc.get_traced_memory())
    tracemalloc.stop()

except Exception as e:
    print("Error: ",e)







