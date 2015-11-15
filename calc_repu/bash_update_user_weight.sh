#! /bin/tcsh

rm out/*
rm err/*
rm temweight/*

foreach VAR(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48)
	bsub -W 2500 -n 4 -o ./out/$VAR.out.%J -e ./err/$VAR.err.%J mpiexec -n 4 $PYTHON deltaR.py run $VAR
end

