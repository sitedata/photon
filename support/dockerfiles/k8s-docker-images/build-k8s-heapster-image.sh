#!/bin/bash

set -e

DIST_TAG=$1
DIST_VER=$2
SPEC_DIR=$3
STAGE_DIR=$4
PH_BUILDER_TAG=$5
ARCH=x86_64

source common.sh

# Docker images for heapster - kubernetes cluster monitoring tool.
fn="${SPEC_DIR}/heapster/heapster.spec"
K8S_HEAPSTER_VER=$(get_spec_ver "${fn}")
K8S_HEAPSTER_VER_REL=${K8S_HEAPSTER_VER}-$(get_spec_rel "${fn}")
K8S_HEAPSTER_RPM=heapster-${K8S_HEAPSTER_VER_REL}${DIST_TAG}.${ARCH}.rpm
K8S_HEAPSTER_RPM_FILE=${STAGE_DIR}/RPMS/${ARCH}/${K8S_HEAPSTER_RPM}

if [ ! -f ${K8S_HEAPSTER_RPM_FILE} ]; then
  echo "Kubernetes HEAPSTER RPM ${K8S_HEAPSTER_RPM_FILE} not found. Exiting.."
  exit 1
fi

IMG_NAME=vmware/photon-${DIST_VER}-k8s-heapster-amd64:${K8S_HEAPSTER_VER}
IMG_ID=$(docker images -q ${IMG_NAME} 2> /dev/null)
if [[ ! -z "${IMG_ID}" ]]; then
  echo "Removing image ${IMG_NAME}"
  docker rmi -f ${IMG_NAME}
fi

mkdir -p tmp/k8heapster
cp ${K8S_HEAPSTER_RPM_FILE} tmp/k8heapster/
pushd ./tmp/k8heapster
cmd="cd '${PWD}' && rpm2cpio '${K8S_HEAPSTER_RPM}' | cpio -vid"
if ! rpmSupportsZstd; then
  docker run --rm --privileged -v ${PWD}:${PWD} $PH_BUILDER_TAG bash -c "${cmd}"
else
  eval "${cmd}"
fi
popd

start_repo_server

K8S_TAR_NAME=k8s-heapster-${K8S_HEAPSTER_VER_REL}.tar
docker build --rm -t ${IMG_NAME} -f ./Dockerfile.heapster .
docker save -o ${K8S_TAR_NAME} ${IMG_NAME}
gzip ${K8S_TAR_NAME}
mv -f ${K8S_TAR_NAME}.gz ${STAGE_DIR}/docker_images/

rm -rf ./tmp
