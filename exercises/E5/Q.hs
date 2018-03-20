module E5.Q where

import Lib

bruteforce = take 1 $ filter (\x -> all (\y -> mod x y == 0) [2..20]) [1..]

clever = foldl lcm 1 [2..20]

solve = clever
