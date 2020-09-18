set term tikz standalone size 10cm, 2cm fontscale 0.5
set xrange [0:100]

set title 'Comparison of $ \cos (\sqrt{x}) $ and $ \sin (\sqrt{x}) $'
set ylabel 'function value'
set xlabel '{$ x $}'
set output 'example.tex'
plot [0:100] cos(sqrt(x)) title '$ \cos (\sqrt{x}) $' lw 3,\
    [0:100] sin(sqrt(x)) title '$ \sin (\sqrt{x}) $' linetype 4 dashtype 2 lw 2

unset output
!pdflatex example