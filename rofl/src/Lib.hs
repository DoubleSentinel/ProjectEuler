module Lib where

intSqrt = floor . sqrt . fromIntegral

primeFactors 1 = []
primeFactors n =
    case factors of
        [] -> [n]
        _ -> factors ++ primeFactors (div n $ head factors)
    where
        factors = take 1 $ filter (\a -> (mod n a) == 0) (2:[3, 5 .. sqrtN])
        sqrtN = intSqrt n

isPalindrome n = show n == reverse (show n)
