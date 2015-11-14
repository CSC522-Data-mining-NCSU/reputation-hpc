#! /bin/tcsh

rm out/*
rm err/*
rm temgrade/*

foreach VAR (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17)
  bsub -W 200 -n 4 -o ./out/$VAR.out.%J -e ./err/$VAR.err.%J mpiexec -n 4 $PYTHON  te.py run $VAR
end
