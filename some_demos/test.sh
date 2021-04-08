#!bin/bash
#if test -d /Users/guozhuangzhi/Desktop/demo
#then
#    echo 'hello'
#fi
#if [ ! -d hello ];
#then
#    echo 'not found'
#else
#    echo 'what?'
#    exit 1
#fi
#
#if [ ! -d hello ];
#then
#    echo 'not found'
#    exit 1
#else
#    echo 'what?'
#fi
#if [ "test -d /Users/guozhuangzhi/Downloads/hello" ]
#then
#    echo 'directory exists'
#    exit 1
#else
#    mkdir /Users/guozhuangzhi/Downloads/hello
#fi
#mv /Users/guozhuangzhi/Desktop/demo/hello /Users/guozhuangzhi/Downloads/

test -d /Users/guozhuangzhi/Desktop/demo/hello && rm -rf /Users/guozhuangzhi/Desktop/demo/hello
