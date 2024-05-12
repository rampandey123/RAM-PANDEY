!! Extra options
gprint, orbitals=0, civec, basis
gthresh,thrprint=0
!!!

basis=cc-pvtz !Basis set

! Molecule xyz file
geometry={
include,/home/matheus/RAM_tests/C2H4_mp2.xyz,echo
}

! Methods
{hf
wf,15,3,1
}
 
{ccsd
wf,15,3,1
}
