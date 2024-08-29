from faker import Faker
import pandas as pd

fake = Faker()
kr_fake = Faker('ko_KR')
Faker.seed()

data_cnt = 10000

name = [kr_fake.name() for i in range(data_cnt)]
username = [fake.user_name() for i in range(data_cnt)]

df = pd.DataFrame()
df['user_id'] = username
df['user_name'] = name

df.to_csv("dummy.csv", encoding='utf-8')