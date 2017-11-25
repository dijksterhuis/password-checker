#!/bin/bash

path=$1
name=$2
tag=$3

echo 'path to build in: '$path
echo 'building: '$name
echo 'tag: '$tag
echo 'build context: ' $(pwd)
echo '+++---+++---+++---+++---+++---+++---+++'
echo 'BUILDING......'
docker build --no-cache -t $name:$tag $path/
