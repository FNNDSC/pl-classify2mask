import shlex
from pathlib import Path
from typing import Iterable
import subprocess as sp
from loguru import logger


class Nums2Mask:

    TOL = 0.5
    """
    Float toleration. MINC is wildly inaccurate when it comes to storing floats,
    so to check if ``A == N``, we need to actually check ``N - 0.5 < A < N + 0.5``
    """

    def __init__(self, ops: dict[str, list[int]]):
        self.__ops = ops

    def nums2mask(self, seg: Path, out: Path) -> int:
        # extract a single mask
        if '' in self.__ops:
            return self._run_minccalc(seg, out, self.__ops[''])

        if self._is_only_in_dir(seg):
            output_dir = out.parent
        else:
            output_dir = out.parent / out.stem
            output_dir.mkdir()

        to_ret = 0
        for name, values in self.__ops.items():
            output_mask = output_dir / name
            rc = self._run_minccalc(seg, output_mask, values)
            to_ret = max(to_ret, rc)

        return to_ret

    def _run_minccalc(self, seg: Path, mask: Path, values: Iterable[int]) -> int:
        cmd = [
            'minccalc', '-quiet', '-unsigned', '-byte', '-range', '0', '1',
            '-expression', self.assemble_calc(values), str(seg), str(mask)
        ]
        p = sp.run(cmd)
        if p.returncode == 0:
            logger.info('MASK {} -> {}', seg, mask)
        else:
            logger.error('!!!FAILED!!! {}', shlex.join(cmd))
        return p.returncode

    @classmethod
    def assemble_calc(cls, values: Iterable[int]) -> str:
        return '||'.join(cls._approx_calc(v) for v in values)

    @classmethod
    def _approx_calc(cls, v: int) -> str:
        # return f'(A[0]>{v - 0.5}&&A[0]<{v + 0.5})'
        return f'segment(A[0],{v - cls.TOL},{v + cls.TOL})'

    def _is_only_in_dir(self, input_file: Path) -> bool:
        glob = input_file.parent.glob(f'*{input_file.suffix}')
        other_files = filter(lambda p: p != input_file, glob)
        return next(other_files, None) is None


assert Nums2Mask.assemble_calc([2]) == 'segment(A[0],1.5,2.5)'
assert Nums2Mask.assemble_calc([2, 3]) == 'segment(A[0],1.5,2.5)||segment(A[0],2.5,3.5)'
assert Nums2Mask.assemble_calc([2, 3, 7]) == 'segment(A[0],1.5,2.5)||segment(A[0],2.5,3.5)||segment(A[0],6.5,7.5)'
