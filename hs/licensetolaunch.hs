import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [Int]
readInput s = (map read) $ words $ last $ lines s

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: [Int] -> Int
solve l = snd $ head $ sort (zip l [0..])
