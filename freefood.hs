import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [[Int]]
readInput = (map (map read . words)) . tail . lines

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: [[Int]] -> Int
solve = length . group . sort . accumulate

accumulate :: [[Int]] -> [Int]
accumulate [] = []
accumulate (x@(s:e:[]):xs) = [s..e] ++ accumulate xs