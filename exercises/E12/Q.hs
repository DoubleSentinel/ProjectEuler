module E12.Q where

import Lib

solve = head $ filter ((>500) . length . factors) triangleNumbers
