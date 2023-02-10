from dataset.problems import Problem, problems

if __name__ == "__main__":
    for problem in problems:
        print(problem.japanese)
        print(problem.english)
        print('----------------')
