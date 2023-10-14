import sys
from pathlib import Path
__all__ = [x.stem for x in Path(Path(__file__).absolute().parent).glob('*.py') if not str(x).startswith('__init')]
if str(Path(__file__).absolute().parent) not in sys.path:sys.path.insert(1, str(Path(__file__).absolute().parent))
