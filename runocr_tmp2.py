
#python 간 파라미터 테스트
def main(data):

    print("main:"+data["filename"])  # 받은 파라미터
    return_data = {"key1":"ok","key2":"main:"+data["filename"]} #return 도 dict type으로 전송
    return return_data

if __name__ == "__main__":
    data = {"filename":"aaaaa","key2":"v2"}
    main(data)
