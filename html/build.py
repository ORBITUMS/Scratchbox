import base64
import re
from pathlib import Path

INPUT_HTML = "localindex.html"  # поменяй, если файл называется иначе
OUTPUT_HTML = "Космос_3D.html"
LIBS_DIR = Path("libs")


def to_data_uri(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:text/javascript;base64,{data}"


orbit_path = LIBS_DIR / "controls" / "OrbitControls.js"
if not orbit_path.exists():
    orbit_path = LIBS_DIR / "OrbitControls.js"

three_uri = to_data_uri(LIBS_DIR / "three.module.js")
orbit_uri = to_data_uri(orbit_path)

html = Path(INPUT_HTML).read_text(encoding="utf-8")

new_importmap = f"""<script type="importmap">
      {{
        "imports": {{
          "three": "{three_uri}",
          "three/addons/controls/OrbitControls.js": "{orbit_uri}"
        }}
      }}
    </script>"""

patched_html, count = re.subn(
    r'<script\s+type="importmap">.*?</script>',
    new_importmap,
    html,
    count=1,
    flags=re.DOTALL,
)

if count == 0:
    raise RuntimeError('В HTML не найден блок <script type="importmap">')

Path(OUTPUT_HTML).write_text(patched_html, encoding="utf-8")
size_kb = Path(OUTPUT_HTML).stat().st_size / 1024
print(f"Готово: {OUTPUT_HTML} ({size_kb:.1f} КБ)")