suspect_info = {'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}

dead = ['Lucas', 'Bill']

# print(dead in suspect_info.values(0))
print(list(suspect_info.values())[0])