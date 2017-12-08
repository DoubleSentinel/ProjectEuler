module E2.Q where

fibs = map fst $ iterate (\(a, b) -> (b, a + b)) (0, 1)

solve = sum $ filter (even) $ filter (<4000000) $ take 50 fibs
