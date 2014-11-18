# SDSC Rocks slurm roll

## Notes

- This roll currently uses the 'default' Rocks download mechanism to 
get files from forge. However, that mechanism currently assumes that 
the `pwd` **is** the name of the roll. That is not the convention we
adopted for our rolls. Therefore, unlike rolls using pull.mk the 
directory for the sources on forge **contains -roll** in the name.


## Installation Notes


The current roll is designed to install on a rocks system with 

```
        Rocks frontend, called "Rocks Server", 
        Rocks attrtibute  "SLURM_Server=True"  assigned to one node called "Slurm Server"
           The Slurm Server can be the same as the Rocks Server or a Slurm Client
        Rocks compute nodes called "Slurm Client"
```	

### Prerequistits for building the roll:

        munge authentication has to be installed on the system before building the roll.

### Roll Installation:

#### Prerequistits: 	

accounts "munge" and "slurm" have to be created on the system before installing the roll
and must exist on all nodes of the cluster. 
SDSC manages accounts in a central Database, "adduser" will not work on the SDSC HPC systems
thus is not included in the SDSC slurm roll. 
	
The rocks host attribute "SLURM_Server=True" has to be assigned to the node running the Slurm Server
         

Rocks Server: The roll will add 2 global attributes in the Rocks database:

```
		SLURM_ClusterName:                 CLUSTER                     
		SLURM_Servername:                  <Service Node name>
```
	
If the global attributes exist they will not be overwritten. 

The slurm configuration files are propagated by Rocks 411. They must exist on all nodes of the cluster
and must have consistent context. A minimal sample configuration file (slurm.conf) is included.

A description of the nodes and their grouping into partitions is required. 
Once the roll is installed on the Rocks Server, the following sample files need to be 
customized manually before the Slurm Server and Slurm Client nodes are installed:    

```
	   /etc/slurm/nodenames.conf
	   /etc/slurm/partitions.conf
```
	
Any change of any of the slurm configuration files is done on the Rocks Server and 
all nodes have to be synchronized via

```
	rocks sync slurm
```
	              
The slurm code is installed in the default location.
munge, slurm-bank, gwrapper, lua, hwloc will be installed in the roll.

     
Eva Hocks 2014
