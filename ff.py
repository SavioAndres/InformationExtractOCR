import os

aa1 = 'C:/Users/savio/Desktop/Base Exploratoria/fulano/9 Outros - 2016.02.22 016.000.02357.2016.3'
path = 'C:/Users/savio/Desktop/Base Exploratoria/fulano/9 Outros - 2016.02.22 016.000.02357.2016.3/Outros0003.jpg'

print(os.path.dirname(path) + ' text/' + os.path.basename(path))

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents[0:]):
    print("President {}: {}".format(num, name))