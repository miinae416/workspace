import re

def validate_password(password):
    # 정규 표현식 패턴: 최소 하나의 소문자, 대문자, 숫자, 특수문자
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~-]).{8,}$'
    
    if re.match(pattern, password):
        return True
    else:
        return False

# 테스트
password = input("비밀번호를 입력하세요: ")
if validate_password(password):
    print("비밀번호가 유효합니다.")
else:
    print("비밀번호가 유효하지 않습니다. 조건을 확인하세요...")
