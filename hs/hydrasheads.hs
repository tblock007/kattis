import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [[Int]]
readInput s = (map ((map read) . words)) $ init $ lines s

writeOutput :: [Int] -> String
writeOutput = unlines . (map show)

solve :: [[Int]] -> [Int]
solve [] = []
solve ((q@(h:t:[])):qs) = (compute h t):(solve qs)

compute :: Int -> Int -> Int
compute h t
    | (h `mod` 2 == 1) && (t == 0) = -1
    | otherwise = (quot (h + (quot (t + at) 2)) 2) + at + (quot (t + at) 2)
    where
        at = addTails h t

addTails :: Int -> Int -> Int
addTails h t
    | h `mod` 2 == 1 = (6 - (t `mod` 4)) `mod` 4
    | otherwise = (4 - (t `mod` 4)) `mod` 4

