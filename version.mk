ROLLNAME	= slurm
VERSION        :=$(shell bash version.sh -v).17.03.8
RELEASE        :=$(shell bash version.sh -h).beta
COPYRIGHT       = Copyright (c) 2014, The Regents of the University of California.
COLOR		= blue

REDHAT.ROOT	= $(CURDIR)
