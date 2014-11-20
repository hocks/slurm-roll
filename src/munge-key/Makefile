#
# $Id$
#
# @Copyright@
# 
#                               Rocks(r)
#                        www.rocksclusters.org
#                        version 6.1 (Emerald Boa)
# 
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.
# @Copyright@

REDHAT.ROOT = $(CURDIR)/../../

PKGROOT = /usr/sbin
NAME = create-munge-key

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
	install -ma+r $(NAME) $(ROOT)/$(PKGROOT)

clean::
	rm -f $(SCRIPTS)

