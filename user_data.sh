#!/bin/bash
set -e -x
export DEBIAN_FRONTEND=noninteractive
sudo locale-gen pt_BR.UTF-8
sudo apt-get update && apt-get upgrade -y
sudo apt-get install -y python
