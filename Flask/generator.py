import read
import test
import percentage

def create(cr=6, cl=4, vl=6):
    #Read markov from 'database' file
    store_file = open("store.txt")
    store_lines = store_file.readlines()

    #First line in file is list of words
    word_list = store_lines[0].split()
    prob_table = []
    for row in store_lines[1:]:
        table_row = []
        for x in row.split():
            table_row.append(int(x))
        prob_table.append(table_row)


    post_table = percentage.generate_percent(prob_table)
    print("Chorus Repetition")
    chorus_rep = cr#int(input())
    print("Chorus Length ")
    chorus_length = cl#int(input())

    print("Verse Length ")
    verse_length = vl#int(input())

    chorus_section = True

    chorus = read.filter(test.generate_text(word_list, post_table, chorus_length))

    #extra_sections = abs(chorus_rep - verse_rep)

    song = ""

    for j in range(chorus_rep * 2):

        if chorus_section == True:
            print("Chorus: ")
            print(" ")
            print(chorus)
            song += "<h3>Chorus</h3>" + chorus + "<br>"
            chorus_section = False
        else:
            verses = read.filter(test.generate_text(word_list, post_table, verse_length))
            print("Verse: ")
            print(" ")
            print(verses)
            song += "<h3>Verse {}</h3>".format((j + 1) // 2) + verses + "<br>"
            chorus_section = True
    return song


