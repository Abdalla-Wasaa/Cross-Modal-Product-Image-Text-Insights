import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
if __name__ == '__main__':
    content = (ROOT / 'generation_prompt.txt').read_bytes()
    pin = {'version':'1.0.0','algorithm':'sha256','sha256':hashlib.sha256(content).hexdigest(),'encoding':'UTF-8','file':'generation_prompt.txt'}
    (ROOT / 'prompt_pin.json').write_text(json.dumps(pin,indent=2)+'\n')
