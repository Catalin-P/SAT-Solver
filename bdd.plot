 ###########################
   # plotting script simple_sat
   ###########################
   
   reset
   set xrange [0:20]
   
   g(x) = 0.0003*exp(x*log(2))
   
   plot "graphic_bdd.out", g(x)
