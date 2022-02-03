FROM docker.io/fnndsc/mni-conda-base:civet2.1.1-python3.10.2

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-nums2mask" \
      org.opencontainers.image.description="A ChRIS ds plugin to create brain mask from segmentation"

WORKDIR /usr/local/src/pl-nums2mask

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install --use-feature=in-tree-build .

CMD ["nums2mask", "--help"]
