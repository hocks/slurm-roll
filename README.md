# SDSC Rocks slurm roll

## Notes

- This roll currently uses the 'default' Rocks download mechanism to get files from http://forge.sdsc.edu/triton. 
However, that mechanism currently assumes that the `pwd` **is** the name of the roll. That is not the convention 
we adopted for our rolls. Therefore, unlike rolls using pull.mk the directory for the sources on forge 
**contains -roll** in the name.


## Installation Notes


- The current roll is designed to install on a rocks system with 

     * Rocks frontend, called **Rocks Server**, 

     * Rocks attrtibute  "SLURM_Server=True"  assigned to one node called **Slurm Server**
       Set to "False" if the node is no longer assigned as **Slurm Server**. 
       The Slurm Server can be the same as the Rocks Server or a Slurm Client or can be a different node such as a Service Node. 
       

     * Rocks compute nodes called **Slurm Client**
	

- Prerequistits for building the roll:

	munge authentication has to be installed on the system before **building** the roll.

### Roll Installation:

####Prerequistits: 	

- Rocks Server: 
     * The roll should be installed on an existing **Rocks Server**

     * accounts "munge" and "slurm" have to be created on the system before installing the roll and must 
       exist on all nodes of the cluster. SDSC manages accounts in a central Database, "adduser" will 
       not work on the SDSC HPC systems thus is not included in the SDSC slurm roll.
	
     * The rocks host attribute "SLURM_Server=true" should to be assigned to the node 
       running the **Slurm Server**. If no **Slurm Server** is assigned the **Rocks Server** will be used as **Slurm Server** 

     * The roll will add 3 global attributes in the Rocks database.
       If the global attributes exist they will not be overwritten. 
   
```
    SLURM_ClusterName:                 CLUSTER                     
    SLURM_Servername:                  <Slurm Server Node name>
    SLURM_ServerAddress:               <Slurm Server Node Management IP Address>
```

  * The slurm configuration files are propagated by Rocks 411. 
    They must exist on all nodes of the cluster and must have consistent context. 
    A minimal sample configuration file (slurm.conf) is included.

    A description of the nodes and their grouping into partitions is required. Once the roll is installed on the Rocks Server, the following sample files need to be customized manually before the Slurm Server and Slurm Client nodes are installed:    

```
    /etc/slurm/nodenames.conf
    /etc/slurm/partitions.conf
```

	Any change of any of the slurm configuration files is done on the Rocks Server. 
	To propagate the changes to all cluster nodes is acomplished via the command:  

```
	rocks sync slurm
```

- Slurm-Server

     * mysql database will be installed for accounting if the Slurm Server is not running on the Rocks Server.
       If you want to run the Slurm Server on the Rocks Server (frontent) the install will try to add it to the 
       existing mysql database. You may need to check the slurm_acct_db database in the mysql database.  

     * After the installation of the mysql database, accounts and users have to be added using sacctmgr.	
       Deposits to the accounts can be made using the sbank deposit command. Please see the sbank man pages
       for further details. 

     * SLURM Bank, a collection of wrapper scripts to give slurm GOLD like capabilities for managing resources,
       is installed to provide basic banking functionality. 
	              
The slurm code is installed in the default location.
     
Eva Hocks
