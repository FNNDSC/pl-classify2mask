FROM docker.io/fnndsc/pl-nums2mask:base-1

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-nums2mask" \
      org.opencontainers.image.description="A ChRIS ds plugin to create brain mask from segmentation"

WORKDIR /usr/local/src/pl-nums2mask

COPY . .
RUN pip install .

CMD ["nums2mask", "--help"]
