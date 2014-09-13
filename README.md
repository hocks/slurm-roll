# SDSC slurm roll



## Notes

- This roll currently uses the 'default' Rocks download mechanism to 
get files from forge. However, that mechanism currently assumes that 
the `pwd` **is** the name of the roll. That is not the convention we
adopted for our rolls. Therefore, unlike rolls using pull.mk the 
directory for the sources on forge **contains -roll** in the name.

- Roll graph and node files exist but are not populated so while 
the roll will build an ISO it will not install anything... (yet).
