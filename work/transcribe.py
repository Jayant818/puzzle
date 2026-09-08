import sys,time
from faster_whisper import WhisperModel
src,out=sys.argv[1],sys.argv[2]
m=WhisperModel('base.en',device='cpu',compute_type='int8',cpu_threads=8)
segs,info=m.transcribe(src,beam_size=1,vad_filter=True,vad_parameters=dict(min_silence_duration_ms=800))
with open(out,'w') as f:
    for s in segs:
        f.write(f"{s.start:9.1f} {s.end:9.1f} {s.text.strip()}\n"); f.flush()
print('done')
