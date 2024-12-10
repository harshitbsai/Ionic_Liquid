# Ionic_Liquid 
This is part of the Lanthanide separations using Ionic liquids where I developed a GAFF model to describe the inter and intra molecular interactions using antechamber. For this I used GROMACS as the MD Simulation Engine. I optimized the structures using Gaussian and got the partial atomic charges using Restrained ELectrostatic Potential Method. 
# Rsync steps to tranfer files 
Steps to do RSync from the Linux Terminal to Argon: 
1. ssh harshit@10.132.10.79 
2.  rsync -r -avz  hbalantr@beartooth.arcc.uwyo.edu:/gscratch/hbalantr  /var/services/homes/harshit
# Force field files creation for GAFF from Gaussian to InterMol 
Steps to generate the force field files from building the molecule to converting the force field files (Generalized Amber Force Field) as per the MD software use like GROMACS, LAMMPS, etc.

1. Create the molecule in Avogadro software.
2. While creating the structure in Avogadro labelling it and structure creation is very important. Mainly, create the heavy atoms first and then fill the hydrogens accordingly.
3. Once the structure is created and labelling is done properly. Do the energy minimization in Avogadro.
4. Once the energy minimization is done create a Gaussian file form the Avogadro.
5. ****While creating the Gaussian file for the calculation of ESP charges and geometry optimization used this basis set **B3LYP 6-311 ++ g (d, p)**. Mainly for the ESP charges extraction and ESP fit centers use this terminology to generate them. **pop=MK Iop (6/33=2,6/41=10,6/42=10,7/33=1).**
6. ****Once the Gaussian calculation is done use Amber tools for the RESP fitting. RESP. – Restrained Electrostatic Potential.
7. ****To fit the ESP charged and calculate the partial charges for the molecule and generate the. mol2 file which will be further used for the generating amber GAFF force field files. Use this command to do RESP fitting in amber tools using ante chamber **- antechamber fi gout i sample. gout fo mol2 o sample. mol2 c resp**
8. ****Once the mol2 file is generated with the partial charges create a new mol2 file by scaling the charges to 0.8 to account for polarization effects. Once that modified. mol2 file is generated we have to use leap program to generate the amber force field files.

**Procedure for the GAFF Force field files:**

**How to prepare input files for the GAFF force field topology and coordinate files?**

1. **Create a file named** in. As the files will be generated using this leap in the Amber tools.

In the input file write this script.

**source leaprc. gaff**

**mods = loadAmberParams C2M_2_Modifed.frcmod**

**MOL = loadMol2 C2M_2_Modified_Scaled.mol2**

**saveAmberParm MOL C2M_Modifed.prmtop C2M_Modified.inpcrd**

**quit**

1. **Using amber tools submit the job with the commands.**

**parmchk2 -i C2M_2_Modified_Scaled.mol2 -f mol2 -o C2M_2_Modifed.frcmod**

**tleap -f tleap_input.in**

1. **Use parmchk2 we will get the frcmod file generated where we will have all the improper, dihedrals will be generated.**
2. **After this with the tleap command and with the use of frcmod file amber tools will create the prmtop (topology file) and inpcrd (Coordinate file) which we will eventually convert as per the software we use for MD Simulations like LAMMPS or GROMACS.**
3. **How to convert those amber topology and coordinate files to GROMACS or to LAMMPS?**
4. How to install InterMol and convert those files?
5. $ git clone https://github.com/shirtsgroup/InterMol.git
6. $ cd InterMol
7. $ pip install .
8. Use this link to know how to use: https://github.com/shirtsgroup/InterMol
9. In the InterMol we have the file convert.py. With the use of the file and the command we can convert the files.
10. python convert.py – gro_in filename.gro top --lammps
11. These means it takes the gromacs .gro and .top files as input and converts to LAMMPS data file and input file.
