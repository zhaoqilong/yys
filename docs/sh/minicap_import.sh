#!/usr/bin/env bash
ABI=$(adb shell getprop ro.product.cpu.abi | tr -d '\r')
adb push libs/$ABI/minicap /data/local/tmp/
adb push jni/minicap-shared/aosp/libs/android-$SDK/$ABI/minicap.so /data/local/tmp/
adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -h
