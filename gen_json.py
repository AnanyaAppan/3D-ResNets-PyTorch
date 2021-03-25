import json
import glob
import random

# ret = {}
# ret["database"] = {}
# print(glob.glob("../../8_s_clips/*"))
# for category_path in glob.glob("../../8_s_clips/*"):
#     category = category_path.split("/")[-1]
#     for video_id_path in glob.glob("../../8_s_clips/"+category+"/*"):
#         video_id = video_id_path.split('/')[-1].strip('.mp4')
#         ret["database"][video_id] = {}
#         annotations = {}
#         annotations["label"] = category
#         length = len(glob.glob("../../8_s_clips_jpeg/"+category+"/"+video_id+"/*"))
#         annotations["segment"] = [0,length]
#         ret["database"][video_id]["annotations"] = annotations
#         ret["database"][video_id]["subset"] = "training"
# y = json.dumps(ret,indent=4)
# print(y)
# with open('../../8_s_clips_jpeg/Annotations/annotations.json','w') as outfile:
#     json.dump(ret,outfile)
class_to_idx={"Arms up":0,"Lock hands":1,"Move the table":2, "Rolly Polly":3, "Tapping":4, "Touch ear":5, "Touch head":6, "Touchnose":7}
ret = {}
print(glob.glob("../../8_s_clips/*"))
for category_path in glob.glob("../../8_s_clips/*"):
    category = category_path.split("/")[-1]
    for video_id_path in glob.glob("../../8_s_clips/"+category+"/*"):
        video_id = video_id_path.split('/')[-1].strip('.mp4')
        d = {}
        if random.uniform(0, 1) >= 0.2:
            d['subset'] = 'training'
        else :
            d['subset'] = 'testing'
        d['duration'] = 8.0
        d['actions'] = [[class_to_idx[category],0.0,8.0]]
        ret[category+'/'+video_id] = d
y = json.dumps(ret,indent=4)
print(y)
with open('../../8_s_clips_jpeg/Annotations/annotations_charades.json','w') as outfile:
    json.dump(ret,outfile)
        