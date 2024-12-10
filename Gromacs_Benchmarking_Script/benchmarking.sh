#!/bin/bash

#SBATCH --job-name="unbound"
#SBATCH --account=pcg_llps
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --mem=2G
#SBATCH --gres=gpu:1
#SBATCH --partition=beartooth-gpu
#SBATCH --time=10:00:00
#SBATCH --export=ALL
#SBATCH [--mail-user=xxx@uwyo.edu](mailto:--mail-user=xxx@uwyo.edu)
#SBATCH --mail-type=START,END,FAIL

module use /project/pcg_llps/codes/packages/
module load k-lab-gmx/2022.5

UW_SRUN=srun
MY_GMX=gmx_mpi
MY_EXE=mdrun

# Running the Simulation

# 

# Execute GROMACS:

# 

export inputfile='em'

# Run grompp for minimization from outside to make sure the formatting is correct.

gmx_mpi grompp -f em.mdp -c 2tsc_solv_ions.gro -p topol.top -o em.tpr

MDRUN_FLAGS=(-deffnm $inputfile.tpr -s $inputfile.tpr -cpi $inputfile.tpr.cpt -nb gpu)
${UW_SRUN} --ntasks=4 $MY_GMX $MY_EXE -ntomp 8 "${MDRUN_FLAGS[@]}" > $inputfile.out

if [ -e em.tpr.gro ]; then
export inputfile='nvt_eq'
gmx_mpi grompp -f $inputfile.mdp -p topol.top -c em.tpr.gro -r em.tpr.gro -o $inputfile.tpr -maxwarn 4
MDRUN_FLAGS=(-deffnm $inputfile.tpr -s $inputfile.tpr -cpi $inputfile.tpr.cpt -nb gpu -pme gpu -npme 1)
${UW_SRUN} --ntasks=4 $MY_GMX $MY_EXE -ntomp 8 "${MDRUN_FLAGS[@]}" > $inputfile.out
fi

if [ -e nvt_eq.tpr.gro ]; then
export inputfile='npt_eq'
gmx_mpi grompp -f $inputfile.mdp -p topol.top -c nvt_eq.tpr.gro -r nvt_eq.tpr.gro -o $inputfile.tpr -maxwarn 4
MDRUN_FLAGS=(-deffnm $inputfile.tpr -s $inputfile.tpr -cpi $inputfile.tpr.cpt -nb gpu -pme gpu -npme 1)
${UW_SRUN} --ntasks=4 $MY_GMX $MY_EXE -ntomp 8 "${MDRUN_FLAGS[@]}" > $inputfile.out
fi

if [ -e npt_eq.tpr.gro ]; then
export inputfile='npt_prod1'
gmx_mpi grompp -f $inputfile.mdp -p topol.top -c npt_eq.tpr.gro -o $inputfile.tpr -maxwarn 4
MDRUN_FLAGS=(-deffnm $inputfile.tpr -s $inputfile.tpr -cpi $inputfile.tpr.cpt -nb gpu -pme gpu -npme 1)
${UW_SRUN} --ntasks=4 $MY_GMX $MY_EXE -ntomp 8 "${MDRUN_FLAGS[@]}" > $inputfile.out
fi

if [ -e npt_prod1.tpr.gro ]; then
export inputfile='npt_prod2'
gmx_mpi grompp -f $inputfile.mdp -p topol.top -c npt_prod1.tpr.gro -o $inputfile.tpr -maxwarn 4
MDRUN_FLAGS=(-deffnm $inputfile.tpr -s $inputfile.tpr -cpi $inputfile.tpr.cpt -nb gpu -pme gpu -npme 1)
${UW_SRUN} --ntasks=4 $MY_GMX $MY_EXE -ntomp 8 "${MDRUN_FLAGS[@]}" > $inputfile.out
fi

if [ -e npt_prod2.tpr.gro ]; then
exit
else
exit
fi
