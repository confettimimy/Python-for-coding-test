
while True:
    try:
        print(input())
    except EOFError:
        break


# 예외처리 try..except문
# try 블록 안에 평소와 같이 명령을 입력
# 예외 상황에 해당하는 오류 핸들러를 except 블록에 입력


# EOFError
# 출력이 완료되고 아무것도 입력안했을 때 빠져나와야 하므로 except 에 EOFError를 적어 Error가 났을 때 break하는 식으로 구현해야한다.
