module E6.Q where

sqr x = x * x

solve = (sqr $ sum [1..100]) - (sum $ map sqr [1..100])
