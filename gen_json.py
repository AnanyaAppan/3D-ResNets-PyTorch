import json
import glob

ret = {}
ret["database"] = {}
print(glob.glob("./*"))
for category_path in glob.glob("./*"):
    category = category_path.split("/")[-1]
    for video_id_path in glob.glob("./"+category+"/*"):
        video_id = video_id_path.split('/')[-1].strip('.mp4')
        ret["database"][video_id] = {}
        annotations = {}
        annotations["label"] = category
        length = len(glob.glob("../8_s_clips_jpeg/"+category+"/"+video_id+"/*"))
        annotations["segment"] = [0,length]
        ret["database"][video_id]["annotations"] = annotations
        ret["database"][video_id]["subset"] = "training"
y = json.dumps(ret,indent=4)
print(y)
with open('./Annotations/annotations.json','w') as outfile:
    json.dump(ret,outfile)
        