module E7.Q where

import Lib

solve = last $ take 10001 $ filter isPrime (2:[3, 5 ..])
