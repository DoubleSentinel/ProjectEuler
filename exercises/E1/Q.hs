module E1.Q where

solve = sum [i | i <- [1..999], mod i 3 == 0 || mod i 5 == 0]
