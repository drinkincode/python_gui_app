import csv
def read_csv(path = 'bingo_words.csv') -> list[str]:
    text_list = []
    with open(path, mode ='r')as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            text_list.append(line)
    return text_list
                        
                    
                        
def write_csv(data: list[str], path: str = 'bingo_words.csv') -> None:
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for line in data:
            writer.writerow([line])


def overwrite_csv(data: list[str], path: str = 'bingo_words.csv') -> None:
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in data:
            writer.writerow([line])