shows = [
    "this   is   an   example ",
    "of   a   paragraph   written   in   ",
    "all   lowercase   letters   ",
    "with   extraaaaaaaa   ",
    "blank   spaces   between   the   words.   it   ",
    "is   often   used   for   formatting  ",
    "exercises,   testing   text   inputs,   or   ",
    "simply   to   illustrate   ",
    "style   changes2."
]

def main():
    cleaned = []
    for line in shows:
        cleaned.append(line.title().strip())

    texttoprint = ''.join(cleaned)
    print(texttoprint)
main()

    
