main = interact (writeOutput . solve . readInput)

readInput :: String -> [Int]
readInput = (map read) . words

writeOutput :: Int -> String
writeOutput = show

solve :: [Int] -> Int
solve (x:y:[]) = (x * (y - 1)) + 1
