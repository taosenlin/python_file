# Time:2020-01-12 15:19
# Author:TSL
for i in range(1,10):
    for j in range(1,i+1):
        print('{} * {} = {}'.format(j,i,i*j),end = '\t')
    print('\n')