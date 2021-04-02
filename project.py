from tkinter import * 
import requests
import json
root=Tk()
api_output_json=json.loads(requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=98d7dddf620240708a5a23ec5dec44fa").content)
i=0
label_bbc=Label(root,text="BBC News Update",font="arial 15 bold").pack()
while True:
    try:
        llb="label_"+str(i)+"_title"
        llb=Label(root,fg="red",font="arial 12 bold",wraplength=700,justify=LEFT)
        llb.pack(anchor="w")
        llb["text"]="Title "+str((i+1))+": "+api_output_json["articles"][i]["title"]
        llb_des="label_"+str(i)+"_des"
        llb_des=Label(root,font="arial 12 bold",wraplength=700,justify=LEFT)
        llb_des.pack(anchor="w")
        llb_des["text"]=api_output_json["articles"][i]["description"]
        i+=1
    except:
        break
root.mainloop()
