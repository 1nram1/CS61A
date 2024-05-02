school = ["CMU","MIT","UCB","STANFORD"]
school_iter = iter(school)
# try:
#     while True:
#         print(next(school_iter))
# except StopIteration:
#     print("No more choices")

for i in school:
    print(i)