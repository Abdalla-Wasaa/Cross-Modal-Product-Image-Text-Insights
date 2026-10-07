from mismatch import ROOT, load_catalog, score_row, write_json

def insight(row):
    result = score_row(row)
    result['seller_message'] = ('Please review the image, title and description together. Confirm brand and product details before editing; this indicator does not establish fraud.' if result['flag'] else 'The manual image tags and listing text agree at the demo threshold. Please confirm the photo and details before publishing.')
    if row.get('transcript_path'):
        path = (ROOT / row['transcript_path']).resolve()
        if ROOT / 'audio' not in path.parents or path.suffix != '.txt':
            raise ValueError('Transcript must be a .txt sidecar inside audio/')
        result['transcript'] = path.read_text().strip()
        result['transcript_source'] = 'txt-sidecar; not Whisper'
    return result
if __name__ == '__main__':
    write_json(ROOT / 'insights.json', [insight(r) for r in load_catalog()])
