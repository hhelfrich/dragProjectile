set term pdfcairo color enhanced font "Times-New-Roman,14" size 5,3
set output "dragPlotGNU.pdf"

set xlabel "{/Times-New-Roman-Italic x}"
set ylabel "{/Times-New-Roman-Italic y}"

plot "dragProjectile.txt" using 2:3 title 'x-y' with lines lw 2

plot "dragProjectile.txt" using 2:4 title  'x-z' with lines lw 2

unset output