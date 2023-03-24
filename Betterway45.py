from datetime import datetime, timedelta


class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds = period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'
    
    def fill(bucket, amount):
        now = datetime.now()
        if (now - bucket.reset_time) > bucket.period_delta:
            bucket.quota = 0
            bucket.reset_time = now
        bucket.quota += amount

    def deduct(bucket, amount):
        now = datetime.now()
        if (now - bucket.reset_time) > bucket.period_delta:
            return False # 새주기가 시작됐는데 아직 버킷 할당량이 재설정되지 않았다
        if bucket.quota - amount < 0:
            return False # 버킷의 가용 용량이 충분하지 못하다
        else:
            bucket.quota -= amount
            return true # 버킷의 가용 용량이 충분하므로 필요한 분량을 사용한다

bucket = Bucket(60)
#     fill(bucket, 100)
#     print(bucket)



# if deduct(bucket, 99):
#     print('99 용량 사용')
# else:
#     print('가용 용량이 작아서 99 용량을 처리할 수 없음')
# print(bucket)


if deduct(bucket, 3):
    print('3 용량 사용')
else:
    print('가용 용량이 작아서 3 용량을 처리할 수 없음')
    
