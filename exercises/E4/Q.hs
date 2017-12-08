module E4.Q where

import Lib

solve = maximum $ filter (isPalindrome) [i * j | i <- [999, 998 .. 990], j <- [999, 998 .. i]]
