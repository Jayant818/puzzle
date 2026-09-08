import sys,json,glob,os
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
ocr=RapidOCR()
def ocr_tiled(path, tile=1280, overlap=160):
    im=Image.open(path).convert('RGB'); W,H=im.size; out=[]
    xs=list(range(0,max(1,W-tile)+1,tile-overlap)); ys=list(range(0,max(1,H-tile)+1,tile-overlap))
    if xs[-1]+tile<W: xs.append(W-tile)
    if ys[-1]+tile<H: ys.append(H-tile)
    for y in ys:
        for x in xs:
            t=np.array(im.crop((x,y,x+tile,y+tile)))
            res,_=ocr(t)
            for r in (res or []):
                out.append((r[1],round(r[2],2),[int(r[0][0][0])+x,int(r[0][0][1])+y]))
    return out
if __name__=='__main__':
    files=sys.argv[2:]; outp=sys.argv[1]
    res={}
    for i,f in enumerate(files):
        res[f]=ocr_tiled(f)
        if i%10==0: json.dump(res,open(outp,'w')); print(i,flush=True)
    json.dump(res,open(outp,'w')); print('done',len(res))
