module Lib where

intSqrt = floor . sqrt . fromIntegral

factors :: Int -> [Int]
factors n = foldl (\acc a -> acc ++ [a, quot n a]) [] $ filter ((==0) . (mod n)) [1..sqrtN]
    where sqrtN = intSqrt n

primeFactors 1 = []
primeFactors n =
    case lFactors of
        [] -> [n]
        _ -> lFactors ++ primeFactors (div n $ head lFactors)
    where
        lFactors = take 1 $ filter (\a -> (mod n a) == 0) (2:[3, 5 .. sqrtN])
        sqrtN = intSqrt n

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n = not $ any (\a -> (mod n a) == 0) (2:[3, 5 .. sqrtN])
    where sqrtN = intSqrt n

isPalindrome n = show n == reverse (show n)

triangleNumbers :: [Int]
triangleNumbers = map triangulate [1..]
    where triangulate n = quot (n * (n + 1)) 2
