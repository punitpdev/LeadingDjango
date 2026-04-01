from pathlib import Path
import requests

def downloader_to_local(url: str, out_path: Path, parent_mkdir: bool = True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path}, must be a valid pathlib")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        responce = requests.get(url)
        responce.raise_for_status()
        out_path.write_bytes(responce.content)
        return True
    except requests.RequestException as a:
        print(f"Failed to download {url}: {a}")
        return False
