def fake_api_request(attempt):
    if attempt==1:
        return 500

    return 200
def test_retry_api_request():
    status_code=fake_api_request(1)
    if status_code == 500:
        status_code = fake_api_request(2)

    assert status_code == 200

#................................................multiple retry

def fake1_api_request(attempt):
    if attempt<3:
        return 500
    return 200
def test_retry1_api_request():
    status_code=500
    for attempt in range(1,4):
        status_code = fake1_api_request(attempt)

        if status_code == 200:
            break

    assert status_code == 200
#................................................................all attemp fail
def test_retry1_all_attempts_fail():
     status_code=500
     for attempt in range(1, 4):
           status_code = 500

     assert status_code == 200

#.............................................................................count attempt
def test_count_api_attempt():
    attempts =0
    for attempt in range(1,4):
        attempts += 1

    assert attempts == 3

#......................................................................

def test_retry_actual_attempts():
    attempts = 0
    status_code = 500

    for attempt in range(1, 4):
        attempts += 1
        status_code = fake1_api_request(attempt)

        if status_code == 200:
            break

    assert attempts == 3
    assert status_code == 200


#..................................................................................

def test_stop_retry_after_three_failures():
    attempts=0
    status_code=500
    for attempt in range(1,4):
        attempts +=1
        status_code=500
    assert attempts==3
    assert status_code==500
