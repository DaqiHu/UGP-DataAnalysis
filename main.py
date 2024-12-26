import csv
import wcwidth
from tabulate import tabulate


def getScore(scoreText) -> float:
    if not isinstance(scoreText, str):
        return float(scoreText)

    newText = scoreText.replace("\xa0", "")
    if not newText.isalpha():
        return float(newText)

    match newText:
        case "优秀":
            return 90.0
        case "良好":
            return 80.0
        case "中等":
            return 70.0
        case "及格":
            return 60.0
        case "不及格":
            return 0.0


def showSubjects(items: list[list[str]], sortBy="semester"):
    titleBar = items[0]
    if sortBy == "score":
        pred = lambda x: getScore(x[8])
    elif sortBy == "credit":
        pred = lambda x: getScore(x[5])
    elif sortBy == "weightedScore":
        pred = lambda x: getScore(x[8]) * getScore(x[5])
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
        total += getScore(item[8]) * getScore(item[5])
        creditTotal += getScore(item[5])
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
    data = [(getScore(i[5]), getCredit(getScore(i[8]))) for i in items]
    return sum([i[0] * i[1] for i in data]) / sum([i[0] for i in data])


def main():
    with open(r"data.csv", newline="", encoding="utf-8") as csvFile:
        dataReader = csv.reader(csvFile)
        data = list(dataReader)

    showSubjects(data, sortBy="weightedScore")

    showSubjects([i for i in data if i[0] == "2A" and getScore(i[8]) < 90], sortBy="weightedScore")

    print("-----------------------------------------------------")
    print(f"加权平均分：    {weightedAverageScore(data):.2f}")
    # term2A = [i for i in data if i[0] == "2A"]
    # showSubjects(term2A, sortBy="credit")
    print(f"加权绩点：      {weightedCredit(data[1:]):.2f}")


if __name__ == "__main__":
    main()
