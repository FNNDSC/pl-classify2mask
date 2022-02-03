# pl-nums2mask

[![Version](https://img.shields.io/docker/v/fnndsc/pl-nums2mask?sort=semver)](https://hub.docker.com/r/fnndsc/pl-nums2mask)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-nums2mask)](https://github.com/FNNDSC/pl-nums2mask/blob/main/LICENSE)
[![Build](https://github.com/FNNDSC/pl-nums2mask/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-nums2mask/actions)

Obtain a mask from selected labels of a segmentation volume.

## Usage

```shell
singularity exec docker://fnndsc/pl-nums2mask nums2mask [-p PATTERN] [-w --values] input/ output/
```

`input/` is a directory which contains segmentations as MINC files.

## Examples

For example, you have a segmentation volume where gray matter (GM) is indicated by
intensity values of 40 and white matter (WM) is indicated by 160. To create a brain mask,
you would need to select the area indicated by the values 40 and 160.

```shell
singularity exec docker://fndsc/pl-nums2mask nums2mask -w 40,160 input/ output/
```

## Development

### Build

```shell
docker build -t localhost/fnndsc/pl-nums2mask .
```

### Get JSON Representation

```shell
docker run --rm localhost/fnndsc/pl-nums2mask chris_plugin_info > nums2mask.json
```

### Local Test Run

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/nums2mask:/usr/local/lib/python3.10/site-packages/nums2mask:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-nums2mask nums2mask -w 1,160 /incoming /outgoing
```
