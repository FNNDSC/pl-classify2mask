# pl-nums2mask

[![Version](https://img.shields.io/docker/v/fnndsc/pl-nums2mask?sort=semver)](https://hub.docker.com/r/fnndsc/pl-nums2mask)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-nums2mask)](https://github.com/FNNDSC/pl-nums2mask/blob/main/LICENSE)
[![Build](https://github.com/FNNDSC/pl-nums2mask/actions/workflows/build.yml/badge.svg)](https://github.com/FNNDSC/pl-nums2mask/actions)

Obtain masks from selected labels of a segmentation volume.
In other words, for input images containing multiple labels e.g. 1=GM, 2=GM,
`nums2mask` can create output images containing single labels like an image containing WM only.

## Usage

```shell
apptainer exec docker://fnndsc/pl-nums2mask nums2mask [-p PATTERN] [-m MASK_SPEC] input/ output/
```

`input/` is a directory which contains segmentations as MINC files.

### `--mask`

`--mask` is a required parameter of `nums2mask`. It is one of:

- a CSV string of integers
- a whitespace-separated list of key-value pairs, separated by `:`, values being CSV-string of integers

## Examples

### Example: Extract One Mask

You have a directory of input MINC segmentation files where white matter (WM) is labeled
by 160 and 5 on the left, and you want to extract left WM masks.

```shell
apptainer exec docker://fndsc/pl-nums2mask nums2mask -m '160,4' input/ output/
```

On an input dataset containing `input/1.mnc input/2.mnc`, the outputs will be
`input/1_mask.mnc input/2_mask.mnc`.

### Example: Extract Multiple Masks

You have a directory of input MINC segmentation files where white matter (WM) is labeled
by 160,4 on the left, and 161,5 on the right. You want to extract left and right WM masks
to the file names "lh.wm.mnc" and "rh.wm.mnc" respectively:

```shell
apptainer exec docker://fndsc/pl-nums2mask nums2mask -m 'lh.wm.mnc:160,4 rh.wm.mnc:161,5' input/ output/
```

On an input dataset containing `input/1.mnc input/2.mnc`, the outputs will be
`output/1/lh.wm.mnc output/1/rh.wm.mnc output/2/lh.wm.mnc output/2/rh.wm.mnc`.

## Development

### Build

```shell
docker build -t localhost/fnndsc/pl-nums2mask .
```

### Get JSON Representation

```shell
docker run --rm localhost/fnndsc/pl-nums2mask chris_plugin_info > nums2mask.json
```
