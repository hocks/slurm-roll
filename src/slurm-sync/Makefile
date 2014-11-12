# @Copyright@
# 
#                               Rocks(r)
#                        www.rocksclusters.org
#                        version 6.1 (Emerald Boa)
# 
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.
# 
# @Copyright@

REDHAT.ROOT = $(CURDIR)/../../

PKGROOT = /opt/rocks/lib/python2.6/site-packages/rocks/commands/sync/slurm/
PLUGINS = $(wildcard *.py)

ifneq ($(RPM.BUILDROOT),)
BUILDROOT = $(RPM.BUILDROOT)
else
BUILDROOT = $(shell pwd)/$(NAME).buildroot
endif

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

build::

install:: 
	mkdir -p $(ROOT)/$(PKGROOT)
	install -ma+r $(PLUGINS) $(ROOT)/$(PKGROOT)

clean::
	rm -f $(SCRIPTS)

