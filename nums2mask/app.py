import os
from pathlib import Path
from argparse import ArgumentParser, Namespace
from chris_plugin import chris_plugin, PathMapper
from concurrent.futures import ThreadPoolExecutor

from nums2mask.helpers import csv2list
from nums2mask.nums2mask import Nums2Mask

parser = ArgumentParser(description='Create brain mask from segmentation volume')
parser.add_argument('-w', '--value', required=True, type=str,
                    help='Voxel values to include in mask as a comma-separated list')
parser.add_argument('-o', '--output-suffix', default='.mask.mnc', type=str,
                    dest='output_suffix',
                    help='output file name suffix')
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
    prog = Nums2Mask(csv2list(options.value))
    with ThreadPoolExecutor(max_workers=len(os.sched_getaffinity(0))) as pool:
        mapper = PathMapper(inputdir, outputdir, glob=options.pattern,
                            suffix=options.output_suffix)
        for seg, mask in mapper:
            pool.submit(prog.nums2mask, seg, mask)
