stn = input()


if ":)" in stn:
    stn = stn.replace(":)","🙂")
if ":(" in stn:
    stn = stn.replace(":(","🙁")

print(stn)
