suspect_info = {'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}

dead = ['Lucas', 'Bill']



def killer(suspect_info, dead):
    for i in range(len(suspect_info)) :
        if set(dead).issubset(set(list(suspect_info.values())[i])) :
            suspect = list(suspect_info.keys())[i]
    return(suspect)

print(killer(suspect_info,dead))