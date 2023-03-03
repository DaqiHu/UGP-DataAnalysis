import csv
import wcwidth
from tabulate import tabulate
with open(r"data.csv", newline="", encoding="utf-8") as csvFile:
    dataReader = csv.reader(csvFile)
    data = list(dataReader)

def showSubjects(items: list[list[str]], sortBy="semester"):
    titleBar = items[0]
    if sortBy == "score":
        pred = lambda x: float(x[8])
    elif sortBy == "credit":
        pred = lambda x: float(x[5])
    elif sortBy == "weightedScore":
        pred = lambda x: float(x[8]) * float(x[5])
    elif sortBy == "semester":
        pred = None
    else:
        print("invalid argument.")
        return
    output = sorted(items[1:], key=pred, reverse=True if sortBy != "semester" else False)
    print(f"\nSorted by {sortBy}:")
    print(tabulate(output, headers=titleBar))

def weightedAverageScore(items: list[list[str]]) -> float:
    total = 0.0
    creditTotal = 0.0
    for item in items[1:]:
        total += float(item[8]) * float(item[5])
        creditTotal += float(item[5])
    return total / creditTotal

def findSubjects(items: list[list[str]], score, above=True) -> list[str]:
    result = []
    for item in items[1:]:
        if above and item[8] >= score:
            result.append(item)
        elif not above and item[8] < score:
            result.append(item)
        
    return result

showSubjects(data)
showSubjects(data, sortBy="score")
showSubjects(data, sortBy="weightedScore")
showSubjects(data, sortBy="credit")

print(f"{weightedAverageScore(data):.2f}")
