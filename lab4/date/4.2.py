import datetime,random
end=datetime.datetime.now()
start=datetime.datetime(2000, 1, 1, 0, 0, 0, 0)
rd=start + (end - start) * random.random()
rd2=end-datetime.timedelta(years=rd)