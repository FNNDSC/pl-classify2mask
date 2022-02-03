from pathlib import Path
from typing import Sequence
import subprocess as sp
from loguru import logger


class Nums2Mask:

    TOL = 0.5
    """
    Float toleration. MINC is wildly inaccurate when it comes to storing floats,
    so to check if ``A == N``, we need to actually check ``N - 0.5 < A < N + 0.5``
    """

    def __init__(self, values: Sequence[int]):
        self.__calc = self.assemble_calc(values)

    def nums2mask(self, seg: Path, mask: Path):
        sp.run(
            [
                'minccalc', '-quiet', '-unsigned', '-byte', '-range', '0', '1',
                '-expression', self.__calc, str(seg), str(mask)
            ],
            check=True
        )
        logger.info('Processed {} -> mask: {}', seg, mask)

    @classmethod
    def assemble_calc(cls, values: Sequence[int]) -> str:
        return '||'.join(cls._approx_calc(v) for v in values)

    @classmethod
    def _approx_calc(cls, v: int) -> str:
        # return f'(A[0]>{v - 0.5}&&A[0]<{v + 0.5})'
        return f'segment(A[0],{v - cls.TOL},{v + cls.TOL})'


assert Nums2Mask.assemble_calc([2]) == 'segment(A[0],1.5,2.5)'
assert Nums2Mask.assemble_calc([2, 3]) == 'segment(A[0],1.5,2.5)||segment(A[0],2.5,3.5)'
assert Nums2Mask.assemble_calc([2, 3, 7]) == 'segment(A[0],1.5,2.5)||segment(A[0],2.5,3.5)||segment(A[0],6.5,7.5)'
