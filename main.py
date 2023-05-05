import csv
import wcwidth
from tabulate import tabulate

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

def weightedCredit(items: list[list[str]]) -> float:
    def getCredit(score: float) -> float:
        if score >= 90.0:
            return 4.0
        elif score >= 85.0:
            return 3.7
        elif score >= 82.0:
            return 3.3
        elif score >= 78.0:
            return 3.0
        elif score >= 75.0:
            return 2.7
        elif score >= 72.0:
            return 2.3
        elif score >= 68.0:
            return 2.0
        elif score >= 60.0:
            return 1.0
        else:
            return 0.0
    
    # (weight, credit)
    data = [(float(i[5]), getCredit(float(i[8]))) for i in items]
    return sum([i[0] * i[1] for i in data]) / sum([i[0] for i in data])

def main():
    with open(r"data.csv", newline="", encoding="utf-8") as csvFile:
        dataReader = csv.reader(csvFile)
        data = list(dataReader)

    showSubjects(data)
    showSubjects(data, sortBy="score")
    showSubjects(data, sortBy="weightedScore")
    showSubjects(data, sortBy="credit")

    print(f"{weightedAverageScore(data):.2f}")

    term2A = [i for i in data if i[0] == "2A"]
    showSubjects(term2A, sortBy="credit")
    print(f"{weightedCredit(term2A):.2f}")


if __name__ == "__main__":
    main()
