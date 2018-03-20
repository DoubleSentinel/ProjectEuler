module Main where

import E{}.Q
import System.TimeIt

main :: IO ()
main = do
    timeIt $ print solve
