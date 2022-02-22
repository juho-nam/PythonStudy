# with

import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# profile.pickle 을 열어서 profile_file 로 저장을 해두고
# profile_file 내용을 pickle.load 로 불러와서 출력
# close() 가 필요없이 with 문에서 자동으로 close 해줌

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read()) # 파이썬을 열심히 공부하고 있어요