#!/bin/sh
# get file path
cwd=`dirname "${0}"`
expr "${0}" : "/.*" > /dev/null || cwd=`(cd "${cwd}" && pwd)`

gcc ${cwd}/main.cpp -lstdc++ && ${cwd}/a.out

