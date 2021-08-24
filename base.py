import csv


def read_titanic():
    data = {}
    with open("titanic.csv") as titanic_data:
        reader = csv.DictReader(titanic_data, delimiter=',', quotechar="\"")
        for line in reader:
            for k, v in line.items():
                if k not in data:
                    data[k] = []
                data[k].append(v)
    return data


def clean_age(data):
    ages = data["Age"]
    for i, a in enumerate(ages):
        if a == '':
            a = "0"
        ages[i] = float(a)
    data["Age"] = ages


# def clean_age_bad(data):
#     ages = data["Age"]
#     for i, a in enumerate(ages):
#         if a == '':
#             ages[i] = 0
#         else:
#             ages[i] = float(a)
#     data["Age"] = ages


def average_age(data):
    clean_age(data)
    return sum(data["Age"]) / len(data["Age"])

tab_male = []
tab_female = []
def sort_genre(data):
    genres = data["Sex"]
    for i, g in enumerate(genres):
        if g == "male":
            genres[i] = 1
            tab_male.append(genres[i])
        elif g == "female":
            genres[i] = 2
            tab_female.append(genres[i])
    data["Sex"] = genres
    return tab_male, tab_female


def average_male(data):
    sort_genre(data)
    return (len(tab_male) / len(data))

def average_female(data):
    sort_genre(data)
    return (len(tab_female) / len(data))


if __name__ == "__main__":
    titanic_data = read_titanic()
    mean_age = average_age(titanic_data)
    mean_male = average_male(titanic_data)
    mean_female = average_female(titanic_data)

    print("Moyenne d'hommes :", mean_male, "%")
    print("Moyenne de femmes :", mean_female, "%")
    print("Age Moyen :", mean_age)
