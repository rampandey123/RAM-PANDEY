!! Extra options
gprint, orbitals=0, civec, basis
gthresh,thrprint=0
!!!

basis=cc-pvtz !Basis set

! Molecule xyz file
geometry={
include,/home/matheus/RAM_tests/C2H4.xyz,echo
}

! Methods
hf
optg

