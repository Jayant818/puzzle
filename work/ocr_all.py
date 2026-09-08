import glob,json,sys
from rapidocr_onnxruntime import RapidOCR
ocr=RapidOCR()
out={}
files=sorted(glob.glob('frames/f_*.jpg'))
for i,f in enumerate(files):
    try:
        res,_=ocr(f)
    except Exception as e:
        res=None
    out[f]=[(r[1],round(r[2],2),[int(r[0][0][0]),int(r[0][0][1])]) for r in (res or [])]
    if i%100==0:
        json.dump(out,open('ocr_frames.json','w'))
        print(i,flush=True)
json.dump(out,open('ocr_frames.json','w'))
print('done',len(out))
