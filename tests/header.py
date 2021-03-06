from get_request import request_ext
import json

def assertEqual(x, y):
    if (x != y):
        print("fail\n")

def test_single():
    print("get single header test")
    data = request_ext(1, 'header', [0])
    assertEqual(json.loads(data)[0], "ok")

def test_many():
    print("get many headers test")
    data = request_ext(1, 'headers', [1, 0])
    assertEqual(json.loads(data)[0], "ok")

    
if __name__ == "__main__":
    test_single()
    test_many()
