module E9.Q where

solve = head [a*b*(1000-a-b) | a <- [1..999], b <- [1..999], a*a + b*b == (1000-a-b)**2]
