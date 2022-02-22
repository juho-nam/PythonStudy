# Pickle
# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장

import pickle
profile_file = open("profile.pickle", "wb") # b는 binary를 뜻함. 피클을 쓰기 위해선 항상 binary로 해야함
profile = {"이름":"박명수","나이":30,"취미":["축구", "골프","코딩"]}
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()