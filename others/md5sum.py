# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-11

import shlex
import subprocess


def md5sum(filename):
    cmd = "md5sum " + filename
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    print(str(p.stdout.read().split()[0].decode("utf-8")).upper())


md5sum("/home/toby/SampleCSVFile_10600kb.csv")
