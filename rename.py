# import os
# from imutils import paths
# imagePaths = list(paths.list_images("dataset/rdrd"))

# for (i,n) in enumerate(imagePaths):
#     try:
#         name =  n.split(os.path.sep)[-2]
#         os.rename(n, "dataset/{}-{}.jpg".format(i,name))
#     except:
#         pass
# # print(imagePaths)

import os
from imutils import paths
imagePaths = list(paths.list_images("dataset"))

for (i,n) in enumerate(imagePaths):
    name = n.split(os.path.sep)[-1]
    print(name.split("-")[1].split(".")[0])
# print(imagePaths)