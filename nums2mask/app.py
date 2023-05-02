import os
import sys
from pathlib import Path
from argparse import ArgumentParser, Namespace
from chris_plugin import chris_plugin, PathMapper
from concurrent.futures import ThreadPoolExecutor
from loguru import logger

from nums2mask.nums2mask import Nums2Mask
from nums2mask.spec import parse_mask_spec

parser = ArgumentParser(description='Create brain mask from segmentation volume')
parser.add_argument('-m', '--mask', required=True, type=str,
                    help='List of output file names and voxel values to include,'
                         'e.g. "wm_left.mnc:4,160 wm_right.mnc:5,161"')
parser.add_argument('-p', '--pattern', default='**/*.mnc',
                    help='pattern for file names to include')


@chris_plugin(
    parser=parser,
    title='Create Brain Mask from Segmentation',
    category='MRI Processing',
    min_memory_limit='500Mi',
    min_cpu_limit='1000m'
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    try:
        ops = parse_mask_spec(options.mask)
    except ValueError as e:
        logger.error('Invalid value --mask="{}": {}', options.mask, str(e))
        sys.exit(1)

    prog = Nums2Mask(ops)
    with ThreadPoolExecutor(max_workers=len(os.sched_getaffinity(0))) as pool:
        mapper = PathMapper.file_mapper(inputdir, outputdir, glob=options.pattern)
        results = pool.map(lambda t: prog.nums2mask(*t), mapper)

    # raise any Exceptions
    for _ in results:
        pass
