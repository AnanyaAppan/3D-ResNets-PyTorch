import json
import glob
import random
import xml.etree.ElementTree as ET

# ret = {}
# ret["database"] = {}
# print(glob.glob("../../SSBD/ssbd_clip_segment/*"))
# for category_path in glob.glob("../../SSBD/ssbd_clip_segment/*"):
#     category = category_path.split("/")[-1]
#     for video_id_path in glob.glob("../../SSBD/ssbd_clip_segment/"+category+"/*"):
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
class_to_idx={"ArmFlapping":0,"HeadBanging":1,"Spinning":2}
# class_to_idx={"Arms up":0,"Lock hands":1,"Move the table":2, "Rolly Polly":3, "Tapping":4, "Touch ear":5, "Touch head":6, "Touchnose":7}
ret = {}
print(glob.glob("../../SSBD/ssbd_clip_segment/data/*"))
for category_path in glob.glob("../../SSBD/ssbd_clip_segment/data/*"):
    category = category_path.split("/")[-1]
    for video_id_path in glob.glob("../../SSBD/ssbd_clip_segment/data/"+category+"/*"):
        video_id = video_id_path.split('/')[-1]
        d = {}
        xml_file = '../../SSBD/Annotations/'+video_id+'.xml'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        if random.uniform(0, 1) >= 0.2:
            d['subset'] = 'training'
        else :
            d['subset'] = 'testing'
        d['duration'] = int(root.find('duration').text.strip('s'))
        # d['actions'] = [[class_to_idx[category],0.0,8.0]]
        d['actions'] = []
        behaviours = root.find('behaviours')
        for behaviour in behaviours:
            time = int(behaviour.find('time').text.split(':')[0].lstrip('0'))
            l = [class_to_idx[category],time]
            d['actions'].append(l)
        for i in range(len(d['actions'])):
            if(i != len(d['actions'])-1):
                d['actions'][i].append(d['actions'][i+1][1])
        d['actions'][-1].append(d['duration'])
        ret[category+'/'+video_id] = d
y = json.dumps(ret,indent=4)
print(y)
with open('../../SSBD/Annotations/annotations_charades.json','w') as outfile:
    json.dump(ret,outfile)
        