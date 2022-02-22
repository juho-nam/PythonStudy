# 파일입출력

# score_file = open("score.txt", "w", encoding="utf8") # "w"는 쓰기. 덮이쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # "a"는 append. 뒤에 이어 쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # .read는 파일의 내용을 모두 읽어옴
# score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 몇 줄인지 모를 때 하는 방법
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 리스트에 값을 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100