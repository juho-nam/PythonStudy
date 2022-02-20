# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩" 입니다.
print('저는 "나도코딩"입니다.') # 가능은 하지만 큰따옴표만 써왔으므로 헷갈릴 수 있음
print("저는 \"나도코딩\"입니다.") # " 앞에 \를 넣는다

# \\ : 문장 내에서 \
#C:\Users\user\Desktop\PythonStudy>
print("C:\\Users\\user\\Desktop\\PythonStudy>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple
# Red Apple 을 적고 커서를 맨 앞으로 가져와 \r 뒤의 문자만큼 덮어씀

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple