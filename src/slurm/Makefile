# Don't re-import Rules-linux-centos.mk
__RULES_LINUX_CENTOS_MK = yes

REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

ifeq ($(REDHAT.ROOT),)
REDHAT.ROOT     = /usr/src/redhat
endif
ifeq ($(REDHAT.VAR),)
REDHAT.VAR      = /var
endif

REDHAT.SOURCES  = $(REDHAT.ROOT)/SOURCES
REDHAT.SPECS    = $(REDHAT.ROOT)/SPECS
REDHAT.BUILD    = $(REDHAT.ROOT)/BUILD
REDHAT.RPMS     = $(REDHAT.ROOT)/RPMS
REDHAT.SRPMS    = $(REDHAT.ROOT)/SRPMS

ifneq ($(RPM.BUILDROOT),)
BUILDROOT = $(RPM.BUILDROOT)
else
BUILDROOT = $(shell pwd)/$(NAME).buildroot
endif

HOME	= $(CURDIR)

.PHONY: $(HOME)/.rpmmacros
$(HOME)/.rpmmacros:
	rm -f $@
	@echo "%_topdir $(REDHAT.ROOT)" > $@
	@echo "%_buildrootdir $(BUILDROOT)" >> $@
	@echo "%buildroot $(BUILDROOT)" >> $@
	@echo "%_var    $(REDHAT.VAR)" >> $@
	@echo "%debug_package   %{nil}" >> $@

rpm: $(HOME)/.rpmmacros
	rpmbuild -ta $(NAME)-$(VERSION).$(TARBALL_POSTFIX)

clean::
	rm -f $(HOME)/.rpmmacros
