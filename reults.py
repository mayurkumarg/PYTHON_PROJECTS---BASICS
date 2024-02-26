print("ᴇxᴀᴍ ʀᴇsᴜʟᴛs!")
name=input("name of the student:")
reg_no=input("reg.no:")
res={"105me21045":"first class","105me21046":"pass","105me21050":"distintion"}
if name=="sharath":
	if reg_no=="105me21045":
	    print("result>>",res["105me21045"])
elif name=="xyz":
    if reg_no=="105me21046":
        print("result>>",res["105me21046"])
elif name=="abc":
    if reg_no=="105me21050":
        print("result>>",res["105me21050"])
else :
    print(f"{name} and {reg_no} mismatch")