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

PKGROOT = /usr/bin
NAME = gwrapper

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


install:: 
	mkdir -p $(ROOT)/$(PKGROOT)
	install -ma+rx $(NAME) $(ROOT)/$(PKGROOT)
	ln -s $(PKGROOT)/$(NAME) $(ROOT)/$(PKGROOT)/gbalance
	ln -s $(PKGROOT)/$(NAME) $(ROOT)/$(PKGROOT)/gdeposit
	ln -s $(PKGROOT)/$(NAME) $(ROOT)/$(PKGROOT)/gstatement
	ln -s $(PKGROOT)/$(NAME) $(ROOT)/$(PKGROOT)/mybalance

build::
	/bin/true

clean::
	rm -f $(SCRIPTS)




