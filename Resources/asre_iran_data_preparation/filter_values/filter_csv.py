import csv


def num_of_word(text):
    result = 0
    paragraphs = text.split('\n')
    for p in paragraphs:
        result += len(p.split(' '))
    return result


def is_valid(row):
    text, summary_2, summary_1, *_ = row
    condition_1 = num_of_word(text) <= 2500
    condition_2 = num_of_word(summary_2) >= 10 or num_of_word(summary_1) >= 10
    return condition_1 and condition_2


with open('phase_1.csv', 'r', encoding='utf-8', newline='') as r, open('phase_2.csv', 'w', encoding='utf-8',
                                                                     newline='') as w:
    reader = list(csv.reader(r))
    writer = csv.writer(w)
    writer.writerow(reader[0])
    for row in reader[1:]:
        if is_valid(row):
            writer.writerow(row)
