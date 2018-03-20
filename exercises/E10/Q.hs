module E10.Q where

import Lib

solve = sum $ filter isPrime [2..2000000]
