import os

def make_commit(days: int):
    if days < 1:

        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as files:
            files.write(f'{dates}\n')


            os.system('git add data.txt')


            os.system('git commit --dates="'+dates+'" -m "Frist Commit"')

            return days * make_commit(days-1)

make_commit(895)
