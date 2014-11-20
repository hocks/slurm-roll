
if [ ! -f "$ROLLSROOT/../../bin/get_sources.sh" ]; then
	echo "To compile this roll on Rocks 6.1.1 or older you need to install a newer rocks-devel rpm.
Install it with:
rpm -Uvh https://googledrive.com/host/0B0LD0shfkvCRRGtadUFTQkhoZWs/rocks-devel-6.2-3.x86_64.rpm
If you need an older version of this roll you can get it from:
https://github.com/rocksclusters-attic"
	exit 1
fi

export SURL=http://forge.sdsc.edu/triton

. $ROLLSROOT/etc/bootstrap-functions.sh

