#
#    Copyright (C) 2011-2012  Werner Saar (wernsaar@googlemail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    
#       "This product includes software developed by the Rocks(r)
#       Cluster Group at the San Diego Supercomputer Center at the
#       University of California, San Diego and its contributors."
#
#
#################################################################################
# Changelog
# v1.1 saar 2011/11/03
#      removed rocks report slurmheadnode > /etc/slurm/headnode.conf
#      removed rocks report slurmdbd > /etc/slurm/slurmdbd.conf
#      added force to make -C /var/411
#      removed scontrol reconfigure
#      added service slurm reconfig >/dev/null
#      added /opt/rocks/bin/tentakel service slurm reconfig >/dev/null
#		
# v1.1.1 saar 2011/11/04
#	changed service slurm reconfig to service slurm restart
#
# v1.1.2 saar 2012/04/09
#       replaced tentakel by pdsh
#       because tentakel is broken
#

import sys
import socket
import rocks.commands.report
import os
import hostlist


class Command(rocks.commands.report.command):
    """
    """
    
    def run(self, params, args):
#	os.system("rocks report slurmnodes > /etc/slurm/nodenames.conf")	
#	os.system("rocks report slurmpartitions > /etc/slurm/partitions.conf")	
	os.system("make -C /var/411 force >/dev/null")
	os.system("sleep 10")
	os.system("service slurm restart >/dev/null")
	#os.system("/opt/rocks/bin/tentakel service slurm reconfig >/dev/null")
	query=('select nodes.name from nodes, memberships where nodes.membership = memberships.id and memberships.name like "%Compute%" order by rack,rank' )
        self.db.execute(query)
        myhostlist = []
        nodelist=0
        for name in self.db.fetchall():
               myhostlist.append("%s" % (name))
               nodelist=1

        if nodelist > 0:
              hl = hostlist.collect_hostlist(myhostlist)
	      os.system("/opt/pdsh/bin/pdsh -w %s service slurm reconfig" % (hl)) 



	

RollName = "slurm"

